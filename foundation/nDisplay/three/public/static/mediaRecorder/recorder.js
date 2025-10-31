class Recorder {
    constructor(permissionGivenCallback, canvas, audioContext) {
        /**
         * Lifted from 
         * https://developer.mozilla.org/en-US/docs/Web/API/MediaRecorder
         * https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getDisplayMedia
         * **/

        const self = this;

        this.format = 'webm';
        this.recordedChunks = [];
        this.secondsPerFrame = 1000;
        this.framePerSecond = 30;
        this.mediaRecorder = null;

        if (audioContext !== undefined) {//this is for basicNoAudio.js
            this.destination = audioContext.createMediaStreamDestination();
        }
        this.source = audioContext.createBufferSource();
        this.source.connect(this.destination);

        const constraints = {
            video:true, audio:true
        };
        let chunks = [];//video chunks

        

        // navigator.mediaDevices
        //     // .getUserMedia(constraints) //getWebCam
        //     .getDisplayMedia(constraints) //getScreenCapture
        //     .then((stream) => {
        //         console.log('permission given! in recorder.js')
        //         self.setupRecorder(stream)
        //         console.log('recorder calling permissionGivenCallback')
        //         permissionGivenCallback();
        //         console.log('recorder called permissionGivenCallback')
        //     })
        //     .catch((err) => {

        //         console.error(`The following error occurred: ${err}`);
        //     });

        // const stream = canvas.captureStream(this.framePerSecond)// this is pure videostream
        const videoStream = canvas.captureStream(this.framePerSecond);
        const stream = new MediaStream([
            ...videoStream.getVideoTracks(),
            ...this.destination.stream.getAudioTracks()
        ]);
        self.setupRecorder(stream)
        permissionGivenCallback();

    }

    setupRecorder(stream) {
        const self = this;
        console.log('setupRecorder')
        if (self.format == 'webm') {//this format also misses some frames at the end of the video, but not as much as mp4...
            this.mediaRecorder = new MediaRecorder(stream, { mimeType: 'video/'+self.format+'; codecs=vp8,opus' }); // Example for WebM with VP8 video and Opus audio
        } else if (self.format == 'mp4') {//this format miss frames at the end of the video...
            this.mediaRecorder = new MediaRecorder(stream, { mimeType: 'video/'+self.format+'; codecs="avc1.424028, mp4a.40.2"' }); // Example for WebM with VP8 video and Opus audio
        } else {
            throw "unhandled format"

        }
        

        this.mediaRecorder.ondataavailable = (event) => {
            if (event.data.size > 0) {
                console.log('this.mediaRecorder.ondataavailable:', event.data.size)
                self.recordedChunks.push(event.data);
            }
        };

        this.mediaRecorder.onstop = () => {
            const blob = new Blob(self.recordedChunks, { type: 'video/'+self.format });
            const url = URL.createObjectURL(blob);
            // You can now download or display the recorded video
            console.log("Recording stopped. Video URL:", url);
            self.recordedChunks = []; // Clear chunks for next recording
        };
        console.log('setupRecorder finished')
    }

    startRecording() {
        if (this.mediaRecorder && this.mediaRecorder.state === 'inactive') {
            this.recordedChunks = [];
            this.mediaRecorder.start(this.secondsPerFrame);
            console.log("Recording started.");
        }
    }

    stopRecording() {
        if (this.mediaRecorder && this.mediaRecorder.state === 'recording') {
            this.mediaRecorder.stop();
            console.log("Recording stopped.");
        }
    }

    sendVideoToBackend(filename) {
        console.log('recordedChunks length: ', this.recordedChunks.length);
        const blob = new Blob(this.recordedChunks, {type: 'video/'+this.format});//webm can be changed to mp4
        const formData = new FormData();
        formData.append('file', blob, filename+'.'+this.format);
        const csrfTokenCookie = getCookie('csrftoken');
        formData.append('csrfmiddlewaretoken', csrfTokenCookie);

        fetch(circuitAnimeRecord_url, {
            method: 'POST',
            body: formData
        }).then(res => console.log("Uploaded: ", res.status));

        this.recordedChunks = []; // Clear chunks for next recording
    }
}

export {Recorder};