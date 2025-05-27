import { data } from "./datum.js";
function svg(width, height, viewBox, content){
    //xmlns="http://wwww.w3.org/2000/svg"
    //xmlns:xlink="htto://www.w3.org/1999/xlink"
    return `<svg width="${width}" height="${height}" viewBox="${viewBox[0]} ${viewBox[1]} ${viewBox[2]} ${viewBox[3]}">${content}</svg>`
}

function rect(x, y, fill, stroke, width, height){
    return `<rect x="${x}" y="${y}" stroke="${stroke}" width="${width}" height="${height}"/>`
}

function circle(cx, cy, r, fill){
    return `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${fill}"/>`
}

function polyline(points, stroke, stroke_width, fill){
    //example points: [[1, 2], [3, 4]]
    const formatted_points = points.reduce((acc, cv) => acc.concat(cv), [])
    return `<polyline points="${formatted_points}" stroke="${stroke}" stroke-width="${stroke_width}" fill="${fill}"/>`
}

function text(x, y, content){
    
    return `<text x="${x}" y="${y}">${content}</text>`
}

