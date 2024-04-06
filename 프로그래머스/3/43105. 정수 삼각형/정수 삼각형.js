function solution(triangle) {
    for (let d = 2; d<= triangle.length; d++){
        for (var i = 0; i<d; i++){
            if (i == 0) triangle[d-1][i] += triangle[d-2][0];
            else if (i == d-1) triangle[d-1][i] += triangle[d-2][d-2];
            else triangle[d-1][i] += Math.max(triangle[d-2][i],triangle[d-2][i-1]);
        }
    }
    
    return Math.max(...triangle[triangle.length-1]);
}