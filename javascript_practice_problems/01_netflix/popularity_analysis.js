function identifyTitles(scores){
    var increasing = true
    var decreasing = true

    for (var i = 0; i < scores.length - 1; i++){
        if (scores[i] > scores[i+1])
            increasing = false
        if (scores[i] < scores[i+1])
            decreasing = false
    }

    return (increasing || decreasing)
}