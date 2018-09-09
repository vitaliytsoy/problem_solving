const romanNumsDictionary ={
  'I': 1,
  'V': 5,
  'X': 10,
  'L': 50,
  'C': 100,
  'D': 500,
  'M': 1000,
};

function romanToDec(romanNum){
  romanNum = romanNum.split('');
  let decimalNum = 0;
  if(romanNum.length === 1) {
    decimalNum = romanNumsDictionary[romanNum[0]];
  } else {
    romanNum.reduce((prev, next, index) => {
      if(romanNumsDictionary[prev] >= romanNumsDictionary[next]){
        decimalNum += romanNumsDictionary[prev];
        if(index === romanNum.length - 1) {
          decimalNum += romanNumsDictionary[next];
        }
      } else {
        decimalNum += romanNumsDictionary[next] - romanNumsDictionary[prev];
      }
      return next;
    });
  }
  return decimalNum;
}
