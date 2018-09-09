var sequence = [];

function decompose(n) {
  sequence = [];
  let isComplete = false;
  let nextDecomposeNum = 0;
  let diffNum = Math.pow(n,2) - 0.1;

  while(!isComplete) {
    [nextDecomposeNum, sqrtList] = findSqrtSeq(diffNum);
    diffNum = Math.round(diffNum) - Math.pow(nextDecomposeNum, 2);

    sequence.push(
      {
        decomposeNum: nextDecomposeNum,
        diffNum: Math.round(diffNum),
        sqrtList: sqrtList
      });

      if(sequence[sequence.length - 1].decomposeNum == 1 && sequence[sequence.length - 1].diffNum != 0) {
        console.log('FIRST CALL');
        if(sequence.length == 1) {
          return null;
        } else {
          sequence.push(reset(n));
        }

        if(sequence[sequence.length - 1].sqrtList.length == 0 && sequence[sequence.length - 1].diffNum != 0) {
          console.log('SECOND CALL');

          if(sequence.length == 1) {
            return null;
          } else {
            sequence.push(reset(n));
          }
        }
        diffNum = sequence[sequence.length - 1].diffNum;
      } else if (sequence[sequence.length - 1].diffNum == 0) {
        sequence.reverse();
        let result = [];
        for(let item of sequence ) {
          result.push(item.decomposeNum);
        }
        console.log(result);

        return result;
      }
  }
}

function findSqrtSeq (diffNum) {
  let nextDecomposeNum = parseInt(Math.sqrt(diffNum));
  let sqrtList = [];

  if(sequence.length !== 0) {
    while(nextDecomposeNum >= sequence[sequence.length - 1].decomposeNum) {
      nextDecomposeNum = nextDecomposeNum - 1;
    }
  }

  for(let i = nextDecomposeNum - 1; i > 0; i--){
    sqrtList.push(i);
  }

  return [nextDecomposeNum, sqrtList];
}


function reset(initialNum) {
  sequence.pop();
  let newDecomposeNum = null;
  let newDiffNum = null;
  let newSqrtList = [];
  var firstDecomposeNum = null;

  if(sequence[sequence.length - 1].sqrtList.length != 0) {
    newDecomposeNum = sequence[sequence.length - 1].sqrtList.shift();
    newSqrtList = sequence[sequence.length - 1].sqrtList;
    sequence.pop();

    if (sequence.length != 0){
      newDiffNum = sequence[sequence.length - 1].diffNum - Math.pow(newDecomposeNum, 2);
    } else {
      newDiffNum = Math.pow(initialNum, 2) - Math.pow(newDecomposeNum, 2);
    }
  }
  return {
    decomposeNum: newDecomposeNum,
    diffNum: newDiffNum,
    sqrtList: newSqrtList
  }
}

function logSequence() {
  for(let item of sequence) {
    console.log(item.decomposeNum + "        " + item.diffNum + "        " + item.sqrtList);
  }
  console.log('\n\n\n\n');
}


function decompose2(n, n2 = n * n, i = n, prev) {
  while (n2 > 0 && i-- > 1) {
    console.log("\n" + n + "     " + n2 + "     " + i  + "     " + prev + '\n');
    if (prev = decompose2(n, n2 - i * i, i)) {
    console.log(n + "     " + n2 + "     " + i  + "     " + prev);
      return prev.concat([i]);
    }
  }
  return (n2 == 0) ? [] : null;
}


decompose2(50);