import re
from string import Template

from foundation.ecircuit.equationFinders.equationfinder import EquationFinder
from video.common.audiofromtext import AudioFromText

import cn2an
from num2words import num2words
import kanjize

mainSymbol__fullName = dict(map(lambda t: (t[1], t[0]), EquationFinder.getMainSymbolMap().items()))
subscript__fullName = dict(map(lambda t: (t[1], t[0]), EquationFinder.getSubscriptSymbolMap().items()))

def translateEquationFinderName(defaultEquationFinderDisplayName, languageTwoLetterCode):#<<<<<<<<<<<<move this to a more global folder... there might be other different animations next time, hopefully mechanical stimulations next =)
    return {
        "Kirchhoff Current Law": {
            'en-US':"Kirchhoff Current Law",
            'zh-CN':"基尔霍夫电流定律",
            'ja-JP':"キルヒホッフの電流法則",
            'de-DE':"Regel von KIRCHHOFF: Knotenregel",
            'fr-FR':"Loi des nœuds (Première loi de Kirchhoff)",
            'ru-RU':"Первое правило Кирхгофа (правило токов Кирхгофа)"
        },
        "Kirchhoff Voltage Law": {
            'en-US':"Kirchhoff Voltage Law",
            'zh-CN':"基尔霍夫电压定律",
            'ja-JP':"キルヒホッフの電圧法則",
            'de-DE':"Regel von KIRCHHOFF: Maschenregel",
            'fr-FR':"Loi des mailles (Deuxième loi de Kirchhoff)",
            'ru-RU':"Второе правило Кирхгофа (правило напряжений Кирхгофа)"
        },
        "Ohm Law": {
            'en-US':"Ohm Law",
            'zh-CN':"欧姆定律",
            'ja-JP':"オームの法則",
            'de-DE':"Ohmsches Gesetz",
            'fr-FR':"la loi d’Ohm",
            'ru-RU':"Закон Ома"
        }

    }[defaultEquationFinderDisplayName][languageTwoLetterCode]


def translateComponentTypeName(componentType, languageTwoLetterCode):
    return {
        "AC_signal_generator":{
            'en-US':"AC signal generator",
            'zh-CN':"交流信号发生器",
            'ja-JP':"交流発生器",
            'de-DE':"WechselstromSignalgenerator",
            'fr-FR':"Générateur de signaux",
            'ru-RU':"Генератор сигналов"
        },
        "battery":{
            'en-US':"battery",
            'zh-CN':"电池",
            'ja-JP':"アルカリ乾電池",
            'de-DE':"Akku",
            'fr-FR':"Piles AA",
            'ru-RU':"аккумуляторов"
        },
        "capacitor":{
            'en-US':"capacitor",
            'zh-CN':"电容器",
            'ja-JP':"コンデンサ",
            'de-DE':"Kondensator",
            'fr-FR':"condensateur",
            'ru-RU':"конденсатор"
        },
        "diode":{
            'en-US':"diode",
            'zh-CN':"二极管",
            'ja-JP':"ダイオード",
            'de-DE':"Diode",
            'fr-FR':"diode",
            'ru-RU':"диод"
        },
        "inductor":{
            'en-US':"inductor",
            'zh-CN':"电感器",
            'ja-JP':"コイル",
            'de-DE':"Spule",
            'fr-FR':"Bobine",
            'ru-RU':"Катушка индуктивности"
        },
        "oscillator":{
            'en-US':"oscillator",
            'zh-CN':"发振器",
            'ja-JP':"オシレーター",
            'de-DE':"Oszillatorschaltung",
            'fr-FR':"oscillateur",
            'ru-RU':"Кварцевый резонатор"
        },
        "resistor":{
            'en-US':"resistor",
            'zh-CN':"电阻器",
            'ja-JP':"抵抗器",
            'de-DE':"Widerstand",
            'fr-FR':"résistance",
            'ru-RU':"Резистор"
        },
        "transistor":{
            'en-US':"transistor",
            'zh-CN':"晶体管",
            'ja-JP':"トランジスター",
            'de-DE':"Transistor",
            'fr-FR':"transistor",
            'ru-RU':"транзистор"
        }
    }[componentType][languageTwoLetterCode]


def translateEliminateVariableToWords(subVar, languageTwoLetterCode):
    regexp = '([a-zA-Z]+)\\_\\{\\s*([a-zA-Z]+)\\_\\{\\s*([0-9]+)\\s*\\}\\s*\\}'
    m = re.search(regexp, subVar)
    if m is None:
        raise Exception('subVar does not fit regex: |'+subVar+'|')
    # print(m.groups())
    main_symbol, subscript, subsubscript = m.groups()

    translatedQuantity = {
        'en-US':{
            'voltage':'voltage',
            'current':'current',
            'resistance':'resistance',
            'capacitance':'capacitance',
            'inductance':'inductance',
            'impedance':'impedance',
            'frequency':'frequency',
            'temperature':'temperature',
            'current_amplification':'current amplification factor'
        },
        'zh-CN':{
            'voltage':'电压',
            'current':'电流',
            'resistance':'电阻',
            'capacitance':'电容',
            'inductance':'电感',
            'impedance':'阻抗',
            'frequency':'频率',
            'temperature':'温度',
            'current_amplification':'电流放大系数'
        },
        'ja-JP':{
            'voltage':'电压',
            'current':'电流',
            'resistance':'电阻',
            'capacitance':'电容',
            'inductance':'电感',
            'impedance':'阻抗',
            'frequency':'频率',
            'temperature':'温度',
            'current_amplification':'电流放大系数'
        },
        'de-DE':{
            'voltage':'Spannung',
            'current':'Strom',
            'resistance':'Widerstand',
            'capacitance':'Kapazität',
            'inductance':'Induktivität',
            'impedance':'Impedanz',
            'frequency':'Frequenz',
            'temperature':'Temperatur',
            'current_amplification':'Stromverstärkungsfaktor'
        },
        'fr-FR':{
            'voltage':'Tension',
            'current':'Courant',
            'resistance':'Résistance',
            'capacitance':'Capacité',
            'inductance':'Inductance',
            'impedance':'Impédance',
            'frequency':'Fréquence',
            'temperature':'Température',
            'current_amplification':'Facteur d’amplification de courant'
        },
        'ru-RU':{
            'voltage':'Напряжение',
            'current':'Ток',
            'resistance':'Сопротивление',
            'capacitance':'Ёмкость',
            'inductance':'Индуктивность',
            'impedance':'Импеданс',
            'frequency':'Частота',
            'temperature':'Температура',
            'current_amplification':'Коэффициент усиления тока'
        }
        
    }[languageTwoLetterCode][mainSymbol__fullName[main_symbol]]

    translatedComponentType = translateComponentTypeName(subscript__fullName[subscript], languageTwoLetterCode) # subscript is the componentType

    # print(languageTwoLetterCode[0:2])
    # import pdb;pdb.set_trace()
    translatedNodeId = num_to_word(int(subsubscript), languageTwoLetterCode[0:2])

    return Template({
        'en-US':"$translatedQuantity of $translatedComponentType $translatedNodeId",
        'zh-CN':"$translatedComponentType$translatedNodeId的$translatedQuantity",
        'ja-JP':"$translatedComponentType$translatedNodeIdの$translatedQuantity",
        'de-DE':"$translatedQuantity am $translatedComponentType $translatedNodeId",
        'fr-FR':"$translatedQuantity de $translatedComponentType $translatedNodeId",
        'ru-RU':"$translatedQuantity на $translatedComponentType $translatedNodeId"
    }[languageTwoLetterCode]).substitute(translatedQuantity=translatedQuantity, translatedComponentType=translatedComponentType, translatedNodeId=translatedNodeId)

def num_to_word(n, lang):
    if lang == 'zh':
        return cn2an.an2cn(n)
    elif lang == 'ja':
        return kanjize.number2kanji(n)
    else:
        return num2words(n, to='cardinal', lang=lang)


def get__language__templateIdx__templates__findEquations():
    return {
        'en-US': {
            0:[
                "Using $equationFinderDisplayName on these circuit elements, we obtain the following formula:", 
                "The following formula is derived from $equationFinderDisplayName, based on these circuit elements:",
                "With these circuit elements and $equationFinderDisplayName, we can get this formula:"
            ],
            1:[
                "The highlighted variable comes from this $componentType, with identity number $nodeId.",
                "This $componentType, with identity number $nodeId, produces this highlighted variable.",
                "The highlighted variable is associated with this $componentType, identity number $nodeId."
            ]
        },
        'zh-CN': {
            0:[
                "将$equationFinderDisplayName应用在这些电路原件上，我们取得这公式：",
                "基于这些电路元件，从$equationFinderDisplayName中可以得出以下公式：",
                "利用这些电路元件和$equationFinderDisplayName，我们可以得到这个公式："
            ],
            1:[
                "标注的变数可以从$nodeId编号的$componentType取得。",
                "$nodeId编号的$componentType让我们取得标注的变数。",
                "我们可以从$nodeId编号的$componentType取得标注的变数。"
            ]
        },
        'ja-JP': {
            0:[
                "これらの電気部品に $equationFinderDisplayName を使用すると、次の公式が得られます。",
                "次の公式は、これらの電気部品によって、$equationFinderDisplayName を付けると、得られます。",
                "$equationFinderDisplayNameで、これらの電気部品に、次の公式が得られます。"
            ],
            1:[
                "強調した未知数は、その$nodeId番号の電気部品の$componentTypeから、出てきます。",
                "その$nodeId番号の電気部品の$componentTypeで、強調した未知数は作れました。",
                "$nodeId番号の電気部品の$componentTypeにおける、強調した未知数は出てきます。"
            ]
        },
        'de-DE': {
            0:[
                "Wenn wir $equationFinderDisplayName auf diesen Bauelementen anwenden, erhalten wir die folgende Formel:",
                "Die folgende Formel wird aus $equationFinderDisplayName abgeleitet, basierend auf diesen Bauelementen:",
                "Mit diesen Bauelementen und $equationFinderDisplayName können wir diese Formel erhalten:"
            ],
            1:[
                "Die hervorgehobene Variable stammt von diesem $componentType mit der Identitätsnummer $nodeId.",
                "Dieser $componentType mit der Identitätsnummer $nodeId erzeugt diese hervorgehobene Variable.",
                "Die hervorgehobene Variable ist mit diesem $componentType, Identitätsnummer $nodeId verknüpft."
            ]
        },
        'fr-FR': {
            0:[
                "Si nous appliquons $equationFinderDisplayName à ces composants, nous obtenons la formule suivante:",
                "La formule suivante est dérivée de $equationFinderDisplayName en fonction de ces composants:",
                "Avec ces composants et $equationFinderDisplayName, nous pouvons obtenir cette formule:"
            ],
            1:[
                "La variable en couleur provient de ce $componentType avec le numéro d'identité $nodeId.",
                "Ce $componentType avec le numéro d'identité $nodeId crée cette variable en couleur.",
                "La variable en couleur est liée à ce $componentType, numéro d'identité $nodeId."
            ]
        },
        'ru-RU': {
            0:[
                "Если мы применим $equationFinderDisplayName к этим компонентам, мы получим следующую формулу:",
                "Следующая формула выведена из $equationFinderDisplayName на основе этих компонентов:",
                "С помощью этих компонентов и $equationFinderDisplayName мы можем получить эту формулу:"
            ],
            1:[
                "Выделенная переменная берется из этого $componentType с идентификационным номером $nodeId.",
                "Этот $componentType с идентификационным номером $nodeId создает эту выделенную переменную.",
                "Выделенная переменная связана с этим $componentType, идентификационный номер $nodeId."
            ]
        }
    }


def generateSubtitle_findEquation(list_equationNetworkInfoDict, textStr__textMeshUUID, nodeId__type, languageTwoLetterCode, introduction, conclusion):

    scripts = []
    scripts.append(introduction)
    for equationFound in list_equationNetworkInfoDict:
        equationFinderDisplayName = translateEquationFinderName(equationFound['equationFinderDisplayName'], languageTwoLetterCode) #<<<<<<<<implement this
        #0 #TODO translate, give another 2 different sentences
        templates0 = language__templateIdx__templates[languageTwoLetterCode][0]
        scriptPart0 = Template(templates0[random.randint(0, len(templates0)-1)]).substitute(equationFinderDisplayName=equationFinderDisplayName)
        scripts.append(scriptPart0)#insert pause?
        #1 # TODO translate, give another 2 different sentences
        #2
        #3 latexEquationString is equationFound['equation'], but the reading might be weird, maybe translate the equation into words
        for variableInfoDict in textStr__textMeshUUID[equationFound['equation']]['info']:
            # print(variableInfoDict); import pdb;pdb.set_trace()
            # for variableStr in variableInfoDict['variables']:
            nodeId = equationFound['variableStr__nodeId'][variableInfoDict['variableStr']]
            componentType = translateComponentTypeName(nodeId__type[nodeId], languageTwoLetterCode)
            #6,8 translate, give another 2 different sentences
            templates1 = language__templateIdx__templates[languageTwoLetterCode][1]
            scriptPart1 = Template(templates1[random.randint(0, len(templates1)-1)]).substitute(componentType=componentType, nodeId=str(nodeId))
            scripts.append(scriptPart1)#insert pause?
            #insert pause<<<<<<<<<<<<<<<<<<<<<
    scripts.append(conclusion)

    return scripts

def generateSubtitles_findEquations(list_equationNetworkInfoDict, textStr__textMeshUUID, nodeId__type, introductions, conclusions):
    """
    list_equationNetworkInfoDict<<<<used to highlight each equation and its associated components
    textStr__textMeshUUID<<<<<<<used to highlight each variable in the equation and its associated component


    Steps by front end are
    0. Highlight network with list_list_networkNodeIds
    1. Display latex equation associated with highlighted_network with equation
    2. pause for a while
    3. unHighlight network 
    4. pause for a while
    5. highlight component representing variable
    6. highlight variable in latex equation
    7. pause for a while
    8. unhighlight variable in latex equation
    """
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<you forgot to add introductions and conclusions
    import random
    language__templateIdx__templates = get__language__templateIdx__templates__findEquations()

    languagesTwoLetterCodes = list(introductions.keys())
    languages__scripts = dict(map(lambda languageCode: (languageCode, []), languagesTwoLetterCodes))
    for languageTwoLetterCode in languagesTwoLetterCodes:
        languages__scripts[languageTwoLetterCode].append(introductions[languageTwoLetterCode])
        for equationFound in list_equationNetworkInfoDict:
            equationFinderDisplayName = translateEquationFinderName(equationFound['equationFinderDisplayName'], languageTwoLetterCode) #<<<<<<<<implement this
            #0 #TODO translate, give another 2 different sentences
            templates0 = language__templateIdx__templates[languageTwoLetterCode][0]
            scriptPart0 = Template(templates0[random.randint(0, len(templates0)-1)]).substitute(equationFinderDisplayName=equationFinderDisplayName)
            languages__scripts[languageTwoLetterCode].append(scriptPart0)#insert pause?
            #1 # TODO translate, give another 2 different sentences
            #2
            #3 latexEquationString is equationFound['equation'], but the reading might be weird, maybe translate the equation into words
            for variableInfoDict in textStr__textMeshUUID[equationFound['equation']]['info']:
                # print(variableInfoDict); import pdb;pdb.set_trace()
                # for variableStr in variableInfoDict['variables']:
                nodeId = equationFound['variableStr__nodeId'][variableInfoDict['variableStr']]
                componentType = translateComponentTypeName(nodeId__type[nodeId], languageTwoLetterCode)
                #6,8 translate, give another 2 different sentences
                templates1 = language__templateIdx__templates[languageTwoLetterCode][1]
                scriptPart1 = Template(templates1[random.randint(0, len(templates1)-1)]).substitute(componentType=componentType, nodeId=str(nodeId))
                languages__scripts[languageTwoLetterCode].append(scriptPart1)#insert pause?
                #insert pause<<<<<<<<<<<<<<<<<<<<<
        languages__scripts[languageTwoLetterCode].append(conclusions[languageTwoLetterCode])

    return languages__scripts



def get__language__templateIdx__templates_solvingSteps():#<<<<<<<<<<<<<<<<move this to another file?
    return {
        'en-US': {
            0:[
                "Our usual method is to take an equation, make the variable we want to eliminate the subject, take another equation and in that, make the variable we want to eliminate the subject, then we join the 2 equations to eliminate that variable. We repeat until we eliminate all the variables we do not want.",
                "A simple method would be to take an equation, and solve for the variable we want to eliminate, and then take another equation, solve for the same variable, then we join the 2 equations together, finally eliminating that variable. And repeat until get rid of all the variables we do not want.",
                "We will take one equation after another, making the variable we want to eliminate the subject of each equation, and at each step joining the two equations, to eliminate the variable. Hopefully at last we will get the formula we want."
            ],
            1:[
                "We have a starting equation with $subLen variables.",
                "We start with this equation with $subLen variables.",
                "Our starting equation has $subLen variables."
            ],
            2:[
                "We want to eliminate variable: $sub",
                "We make $sub the subject, so that we can eliminate it.",
                "We want to eliminate $sub, so we make it the subject."
            ],
            3:[
                "Next, we take this equation and also make $sub as subject.",
                "To eliminate $sub, we make it the subject of this equation.",
                "Now, we make $sub the subject of this equation to eliminate it."
            ],
            4:[
                "Now we join them together.",
                "We combine the two equations together.",
                "Simply join the two equations."
            ],
            5:[
                "And then we keep repeating, so from now, we will just mention the variable that we want to eliminate.",
                "And now we will just keep repeating, eliminating the variables we do not want.",
                "From now, we will just keep eliminating the variables we do not want."
            ],
            6:[
                "In this step, we will eliminate $sub.",
                "Now we will eliminate $sub.",
                "This step eliminates $sub."
            ],
            7:[
                "In this step, we will simplify.",
                "Now, we will simplify.",
                "This is simplifying step."
            ]
        },
        'zh-CN': {
            0:[
                "我们依此术解答：先取一个方程，将需要消去的变数挪为主项，再取另一个方程，将需要消去的变量也挪为主项，然后把两个方程连接起来，消去主项。重复这个程序，直到消去所有不需要的变数。",
                "先取一个方程，解出我们想要消除的变数，然后取另一个方程，解出同样的变数，最后将两个方程连接起来，最终消去该变数。重复此程序，直到消去所有不需要的变数。",
                "我们将逐个解方程，把需要消去的变数作为每个方程的主项，然后每一步将两个方程连接起来，消去该变数。最终我们能得到想要的公式。"
            ],
            1:[
                "这开头方程有$subLen个变数。",
                "我们从有$subLen个变数的方程开始。",
                "我们的开头方程有$subLen个变数。"
            ],
            2:[
                "我们求消去变数$sub。",
                "我们将变数$sub挪为主项，以便把它消去。",
                "我们求消去变数$sub,所以将它挪为主项。"
            ], 
            3:[
                "接下来，我们也将这个方程的$sub挪为主项。",
                "为消去变数$sub，我们也将它挪为主项。",
                "我们也将这个方程的$sub挪为主项以便消去它。"
            ],
            4:[
                "现在我们把两个方程连在一起。",
                "我们将两个方程结合起来。",
                "如今只需将两个方程式相连。"
            ],
            5:[
                "然后我们不断重复，所以于此之后，我们只会提到我们想要消除的变数。",
                "因从此只需不断重复，我们只会提到我们想要消除的变数。",
                "然后，我们只会提到我们想要消除的变数。"
            ],
            6:[
                "于此，我们将消除$sub。",
                "现在我们将消除$sub。",
                "此步骤将消除$sub。"
            ],
            7:[
                "于此，我们将简化方程。",
                "现在我们将简化方程。",
                "这是个简化步骤。"
            ]
        },
        'ja-JP': {
            0:[
                "問題を解くには、まず1つの公式を取り、消去したい変数を表します。次に別の公式を取り、消去したい変数も表します。そして2つの公式を繋ぎ、主項を消去します。このプロセスを、不要な変数がすべて消去されるまで繰り返します。",
                "まず、1つの公式を取り、消去したい変数について解きます。次に、別の公式を取り、同じ変数について解きます。最後に、2つの公式を繋げて、その変数を消去します。不要な変数がすべて消去されるまで、このプロセスを繰り返します。",
                "消去したい変数を各公式の主項として、公式を一つずつ解き、各ステップで2つの公式を繋ぎ合わせて変数を消去していきます。最終的に、求める公式が得られます。"
            ],
            1:[
                "この始める公式には、変数が$subLenある。",
                "変数を$subLen含む公式から始めます。",
                "最初の公式には変数が$subLenあります。"
            ],
            2:[
                "変数を$sub消去したい。",
                "これを削除するには、変数$subを表します。",
                "変数$subを消去したいので、表します。"
            ], 
            3:[
                "次に、この公式の$subを表します。",
                "変数$subを消去するには、表します。",
                "また、$sub を表して消去します。"
            ],
            4:[
                "それでは、2つの公式を結び付けます。",
                "2つの公式を組み合わせます。",
                "さて、2つの公式ををつなげるだけです。"
            ],
            5:[
                "それから、先ほどのプロセスを繰り返しだけので、消去したい変数を除いて、そのいがいのことを触れません。",
                "したがって、これからは、消去したい変数についてのみ言及します。",
                "次に、消去したい変数だけに触れます。"
            ],
            6:[
                "このステップでは$subを消去します。",
                "ここでは$subを消去します。",
                "このステップは、$subが消去されます。"
            ],
            7:[
                "公式を簡単にしましょう。",
                "次に、この公式を簡略化します。",
                "公式を整理します。"
            ]
        },
        'de-DE': {
            0:[
                "Unsere übliche Methode besteht darin, eine Gleichung zu nehmen, die Variabel, die wir eliminieren möchten, zum Subjekt zu machen, eine andere Gleichung zu nehmen und darin die Variabel zu machen, die wir eliminieren möchten, dann verbinden wir die beiden Gleichungen, um diese Variabel zu eliminieren. Wir wiederholen dies, bis wir alle Variabeln eliminiert haben, die wir nicht wollen.",
                "Eine einfache Methode wäre, eine Gleichung zu nehmen und nach der zu eliminierenden Variabel aufzulösen. Dann eine andere Gleichung zu nehmen und nach derselben Variabel aufzulösen. Anschließend verbinden wir die beiden Gleichungen miteinander und eliminieren schließlich diese Variabel. Und wiederholen diesen Vorgang, bis wir alle unerwünschten Variabeln los sind.",
                "Wir werden eine Gleichung nach der anderen durchgehen, die Variabel, die wir eliminieren möchten, zum Subjekt jeder Gleichung machen und bei jedem Schritt die beiden Gleichungen verbinden, um die Variabel zu eliminieren. Hoffentlich erhalten wir schließlich die gewünschte Formel."
            ],
            1:[
                "Wir haben eine Ausgangsgleichung mit $subLen-Variabeln.",
                "Wir beginnen mit dieser Gleichung mit $subLen-Variabeln.",
                "Unsere Ausgangsgleichung hat $subLen-Variabeln."
            ],
            2:[
                "Wir möchten die Variabel eliminieren: $sub.",
                "Wir machen $sub zum Betreff, damit wir es eliminieren können.",
                "Wir möchten $sub eliminieren, also machen wir es zum Betreff."
            ], 
            3:[
                "Als nächstes nehmen wir diese Gleichung und machen auch $sub zum Subjekt.",
                "Um $sub zu eliminieren, machen wir es zum Subjekt dieser Gleichung.",
                "Jetzt machen wir $sub zum Subjekt dieser Gleichung, um es zu eliminieren."
            ],
            4:[
                "Jetzt verbinden wir sie miteinander.",
                "Wir kombinieren die beiden Gleichungen miteinander.",
                "Verbinde einfach die beiden Gleichungen."
            ],
            5:[
                "Und dann wiederholen wir es weiter, also werden wir von nun an nur noch die Variabel erwähnen, die wir eliminieren wollen.",
                "Und jetzt wiederholen wir einfach weiter und eliminieren die Variabeln, die wir nicht wollen.",
                "Von nun an werden wir einfach die Variabeln eliminieren, die wir nicht wollen."
            ],
            6:[
                "In diesem Schritt werden wir $sub eliminieren.",
                "Jetzt werden wir $sub eliminieren.",
                "Dieser Schritt eliminiert $sub."
            ],
            7:[
                "In diesem Schritt vereinfachen wir die Gleichung.",
                "Jetzt vereinfachen wir die Gleichung.",
                "Dies ist ein vereinfachter Schritt."
            ]
        },
        'fr-FR': {
            0:[
                "Notre méthode habituelle consiste à prendre une équation, à faire de la variable à éliminer le sujet, à prendre une autre équation et à faire de la variable à éliminer le sujet, puis à combiner les deux équations pour éliminer cette variable. Nous répétons cette opération jusqu'à ce que nous ayons éliminé toutes les variables indésirables.",
                "Une méthode simple consiste à prendre une équation et à la résoudre pour la variable à éliminer. Ensuite, à prendre une autre équation et à la résoudre pour la même variable. On combine ensuite les deux équations et on élimine finalement cette variable. Et on répète ce processus jusqu'à ce que toutes les variables indésirables soient éliminées.",
                "Nous allons travailler sur une équation à la fois, en faisant de la variable à éliminer le sujet de chaque équation, et à chaque étape, en combinant les deux équations pour éliminer la variable. Nous espérons obtenir la formule souhaitée."
            ],
            1:[
                "Nous avons une équation initiale avec des $subLen variables.",
                "Nous commençons avec cette équation avec les $subLen variables.",
                "Notre équation initiale a $subLen variables."
            ],
            2:[
                "Nous voulons éliminer la variable : $sub.",
                "Nous faisons de $sub le sujet afin de pouvoir l'éliminer.",
                "Nous voulons éliminer $sub, nous en faisons donc le sujet."
            ], 
            3:[
                "Ensuite, nous prenons cette équation et faisons également de $sub le sujet.",
                "Pour éliminer $sub, nous en faisons le sujet de cette équation.",
                "Maintenant, nous faisons de $sub le sujet de cette équation pour l'éliminer."
            ],
            4:[
                "Maintenant, nous les connectons ensemble.",
                "Nous combinons les deux équations.",
                "Il suffit de relier les deux équations."
            ],
            5:[
                "Et puis on continue à le répéter, donc à partir de maintenant on ne mentionnera que la variable qu'on veut éliminer.",
                "Et maintenant, nous continuons simplement à répéter et à éliminer les variables que nous ne voulons pas.",
                "À partir de maintenant, nous éliminerons simplement les variables dont nous ne voulons pas."
            ],
            6:[
                "Dans cette étape, nous allons éliminer $sub.",
                "Nous allons maintenant éliminer $sub.",
                "Cette étape élimine $sub."
            ],
            7:[
                "Dans cette étape, nous simplifions l'équation.",
                "Maintenant, nous simplifions l'équation.",
                "Il s'agit d'une étape simplifiée."
            ]
        },
        'ru-RU': {
            0:[
                "Наш обычный метод заключается в том, чтобы взять одно уравнение, сделать переменную, которую мы хотим исключить, подлежащим, взять другое уравнение и сделать переменную, которую мы хотим исключить, подлежащим, а затем объединить два уравнения, чтобы исключить эту переменную. Мы повторяем этот процесс, пока не исключим все ненужные переменные.",
                "Простой метод — взять одно уравнение и решить его относительно переменной, которую нужно исключить. Затем взять другое уравнение и решить его относительно той же переменной. Затем мы объединяем два уравнения и, наконец, исключаем эту переменную. И повторяем этот процесс, пока не исключим все нежелательные переменные.",
                "Мы будем работать с одним уравнением за раз, делая переменную, которую хотим исключить, объектом каждого уравнения, и на каждом шаге объединяя два уравнения для исключения этой переменной. Надеюсь, в конечном итоге мы получим нужную формулу."
            ],
            1:[
                "У нас есть начальное уравнение с переменными $subLen.",
                "Начнем с этого уравнения с переменными $subLen.",
                "Наше исходное уравнение имеет переменные $subLen."
            ],
            2:[
                "Мы хотим исключить переменную: $sub.",
                "Мы делаем $sub темой, чтобы иметь возможность его исключить.",
                "Мы хотим исключить $sub, поэтому делаем его подлежащим."
            ], 
            3:[
                "Далее мы берем это уравнение и также делаем $sub подлежащим.",
                "Чтобы исключить $sub, мы делаем его субъектом этого уравнения.",
                "Теперь мы делаем $sub объектом этого уравнения, чтобы исключить его."
            ],
            4:[
                "Теперь соединяем их вместе.",
                "Объединяем два уравнения.",
                "Просто соедините два уравнения."
            ],
            5:[
                "И затем мы продолжаем повторять это, так что с этого момента мы будем упоминать только ту переменную, которую хотим исключить.",
                "И теперь мы просто продолжаем повторять и исключать ненужные нам переменные.",
                "С этого момента мы просто удалим те переменные, которые нам не нужны."
            ],
            6:[
                "На этом этапе мы удалим $sub.",
                "Теперь мы устраним $sub.",
                "Этот шаг исключает $sub."
            ],
            7:[
                "На этом этапе мы упрощаем уравнение.",
                "Теперь упростим уравнение.",
                "Это упрощенный шаг."
            ]
        }
    }



def generateSubtitle_solvingStep(solvingSteps, languageTwoLetterCode, introduction, conclusion):
    scripts = []
    language__templateIdx__templates = get__language__templateIdx__templates_solvingSteps()
    templateIdx__templates =language__templateIdx__templates[languageTwoLetterCode]
    def addScriptToList(templateNum, kwargs):
        templates0 = templateIdx__templates[templateNum]
        scriptPart0 = Template(templates0[random.randint(0, len(templates0)-1)]).substitute(**kwargs)
        scripts.append(scriptPart0)#insert pause?
    scripts.append(introduction)
    addScriptToList(0, {})
    #insert pause<<<<<<<<<<<<<<<<<<<<<
    firstStep = solvingSteps[0]['vor']
    # print(firstStep)
    addScriptToList(1, {'subLen':len(firstStep['variables'])})
    translate_variable_to_words = translateEliminateVariableToWords(solvingSteps[1]['sub'], languageTwoLetterCode)
    addScriptToList(2, {'sub':translate_variable_to_words})
    #insert pause<<<<<<<<<<<<<<<<<<<<<
    addScriptToList(3, {'sub':translate_variable_to_words})
    #insert pause<<<<<<<<<<<<<<<<<<<<<
    addScriptToList(4, {})
    addScriptToList(5, {})
    #insert pause<<<<<<<<<<<<<<<<<<<<<
    for stepIdx, solvingStep in enumerate(solvingSteps[1:]):
        # pp.pprint(solvingStep)
        # if solvingStep['stepType']=='solving':
        if solvingStep['sub'] == '':#mainStep is simplification
            addScriptToList(7, {})
        else:
            translate_variable_to_words = translateEliminateVariableToWords(solvingStep['sub'], languageTwoLetterCode)
            addScriptToList(6, {'sub':translate_variable_to_words})

    scripts.append(conclusion)
    return scripts

def generateSubtitles_solvingSteps(solvingSteps, introductions, conclusions):#maybe adding some conjunctions might smoothen the narration?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    """
    0. 'We have a starting equation'
    1. 'We want to eliminate variable: {translate variable to words}'
    2. 'So, we move things around until we have {translate variable to words} as subject'
    3. 'Next, we take this equation and also make {translate variable to words} as subject'
    4. 'Now we join them together'
    5. 'And then we keep repeating, so from now, we will just mention the variable that we want to eliminate'

    Repeats: 'In this step, we will eliminate {translate variable to words}'

    #is it weird to keep repeating the same steps, in different ways? But the variable to eliminate, should be mentioned?
    """
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<you forgot to add introductions and conclusions
    import random
    language__templateIdx__templates = get__language__templateIdx__templates_solvingSteps()
    languagesTwoLetterCodes = list(introductions.keys())
    languages__scripts = dict(map(lambda languageCode: (languageCode, []), languagesTwoLetterCodes))
    def addScriptToList(languageTwoLetterCode, templateNum, kwargs):
        templates0 = language__templateIdx__templates[languageTwoLetterCode][templateNum]
        scriptPart0 = Template(templates0[random.randint(0, len(templates0)-1)]).substitute(**kwargs)
        languages__scripts[languageTwoLetterCode].append(scriptPart0)#insert pause?
    
    #####
    # import pprint
    # pp = pprint.PrettyPrinter(indent=4)

    #####


    for languageTwoLetterCode in languagesTwoLetterCodes:
        #translate
        languages__scripts[languageTwoLetterCode].append(introductions[languageTwoLetterCode])
        addScriptToList(languageTwoLetterCode, 0, {})
        #insert pause<<<<<<<<<<<<<<<<<<<<<
        firstStep = solvingSteps[0]['vor']
        # print(firstStep)
        addScriptToList(languageTwoLetterCode, 1, {'subLen':len(firstStep['variables'])})
        translate_variable_to_words = translateEliminateVariableToWords(solvingSteps[1]['sub'], languageTwoLetterCode)
        addScriptToList(languageTwoLetterCode, 2, {'sub':translate_variable_to_words})
        #insert pause<<<<<<<<<<<<<<<<<<<<<
        addScriptToList(languageTwoLetterCode, 3, {'sub':translate_variable_to_words})
        #insert pause<<<<<<<<<<<<<<<<<<<<<
        addScriptToList(languageTwoLetterCode, 4, {})
        addScriptToList(languageTwoLetterCode, 5, {})
        #insert pause<<<<<<<<<<<<<<<<<<<<<
        for stepIdx, solvingStep in enumerate(solvingSteps[1:]):
            # pp.pprint(solvingStep)
            # if solvingStep['stepType']=='solving':
            if solvingStep['sub'] == '':#mainStep is simplification
                addScriptToList(languageTwoLetterCode, 7, {})
            else:
                translate_variable_to_words = translateEliminateVariableToWords(solvingStep['sub'], languageTwoLetterCode)
                addScriptToList(languageTwoLetterCode, 6, {'sub':translate_variable_to_words})
            # for hinSubStep in solvingStep['hin__subSteps']:
            #     if hinSubStep['stepType'] == 'solving':
            #         print(hinSubStep)
            #         translate_variable_to_words = translateEliminateVariableToWords(hinSubStep['sub'], languageTwoLetterCode)
            #         addScriptToList(languageTwoLetterCode, 6, {'sub':translate_variable_to_words})
            #     else: #simplification step
            #         addScriptToList(languageTwoLetterCode, 7, {})
            # for vorSubStep in solvingStep['vor__subSteps']:
            #     if vorSubStep['stepType'] == 'solving':
            #         translate_variable_to_words = translateEliminateVariableToWords(vorSubStep['sub'], languageTwoLetterCode)
            #         addScriptToList(languageTwoLetterCode, 6, {'sub':translate_variable_to_words})
            #     else: #simplification step
            #         addScriptToList(languageTwoLetterCode, 7, {})

        languages__scripts[languageTwoLetterCode].append(conclusions[languageTwoLetterCode])
    return languages__scripts


def generateAudioFilePath_findEquation(list_equationNetworkInfoDict, textStr__textMeshUUID, nodeId__type, languageTwoLetterCode, introduction, conclusion, folderpath):
    subtitles = generateSubtitle_findEquation(list_equationNetworkInfoDict, textStr__textMeshUUID, nodeId__type, languageTwoLetterCode, introduction, conclusion)
    languages__subtitleIdx__dict_startTime_endTime, languages__filepath, language__pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime = AudioFromText.convert({'languageTwoLetterCode':subtitles}, folderpath)
    return subtitles, languages__subtitleIdx__dict_startTime_endTime[languageTwoLetterCode], languages__filepath[languageTwoLetterCode], language__pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime[languageTwoLetterCode]

def generateAudioFilePaths_findEquations(list_equationNetworkInfoDict, textStr__textMeshUUID, nodeId__type, introductions, conclusions, folderpath):
    languages__subtitles = generateSubtitles_findEquations(list_equationNetworkInfoDict, textStr__textMeshUUID, nodeId__type, introductions, conclusions)
    languages__subtitleIdx__dict_startTime_endTime, languages__filepath, language__pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime = AudioFromText.convert(languages__subtitles, folderpath)
    return languages__subtitles, languages__subtitleIdx__dict_startTime_endTime, languages__filepath, language__pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime


def generateAudioFilePath_solvingStep(solvingSteps, languageTwoLetterCode, introduction, conclusion, folderpath):
    subtitles = generateSubtitle_solvingStep(solvingSteps, languageTwoLetterCode, introduction, conclusion)
    languages__subtitleIdx__dict_startTime_endTime, languages__filepath, language__pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime = AudioFromText.convert({'languageTwoLetterCode':subtitles}, folderpath)
    return subtitles, languages__subtitleIdx__dict_startTime_endTime[languageTwoLetterCode], languages__filepath[languageTwoLetterCode], language__pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime[languageTwoLetterCode]


def generateAudioFilePaths_solvingSteps(solvingSteps, introductions, conclusions, folderpath):
    languages__subtitles = generateSubtitles_solvingSteps(solvingSteps, introductions, conclusions)
    languages__subtitleIdx__dict_startTime_endTime, languages__filepath, language__pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime = AudioFromText.convert(languages__subtitles, folderpath)
    return languages__subtitles, languages__subtitleIdx__dict_startTime_endTime, languages__filepath, language__pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime