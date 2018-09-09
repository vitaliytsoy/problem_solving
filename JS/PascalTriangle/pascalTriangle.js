function pascalsTriangle(n) {
  let result = [];
  for(let i = 1; i <= n; i++) {
    result = result.concat(generateNextRow(result.slice(result.length-i), i));
  }
  return result;
}
function generateNextRow(prevRow, rowNum) {
  let nextRow = [];
  nextRow.length = rowNum;
  [nextRow[0], nextRow[nextRow.length - 1]] = [1, 1];

  for(let [index, item] of nextRow.entries()) {
    if(item === undefined) {
      nextRow[index] = prevRow[index+1] + prevRow[index];
    }
  }
  return nextRow;
}

pascalsTriangle(5);
