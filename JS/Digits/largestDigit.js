function solution(digits){
  let inputDigit = digits.toString();
  let response = {
    "Executive.WorkPhoneNumber": ["The WorkPhoneNumber field is not a valid phone number."],
    "Executive.MobilePhoneNumber": ["The MobilePhoneNumber field is not a valid phone number."]
  }
  for (var property1 in response) {
    console.log(response[property1][0]);
  }


}
solution(1231231);