// One simple way to encrypt a string is to "rotate" every alphanumeric character by a certain amount.
// Rotating a character means replacing it with another character that is a certain number of steps away in normal alphabetic or numerical order.
// For example, if the string "Zebra-493?" is rotated 3 places, the resulting string is "Cheud-726?". Every alphabetic character is replaced with
// the character 3 letters higher (wrapping around from Z to A), and every numeric character replaced with the character 3 digits higher (wrapping around from 9 to 0).
// Note that the non-alphanumeric characters remain unchanged.
// Given a string and a rotation factor, return an encrypted string.

function rotationalCipher(input, rotationFactor) {
  // Write your code here
  let output = [];

  for (const char of input) {
    let encodedVal = 0;
    let encoded = "";

    // upper case letters
    if (char >= "A" && char <= "Z") {
      encodedVal = char.charCodeAt(0) + (rotationFactor % 26);

      if (encodedVal > "Z".charCodeAt(0)) {
        encodedVal -= 26;
      }

      encoded = String.fromCharCode(encodedVal);
      output.push(encoded);
    }
    // lower case letters
    else if (char >= "a" && char <= "z") {
      encodedVal = char.charCodeAt(0) + (rotationFactor % 26);

      if (encodedVal > "z".charCodeAt(0)) {
        encodedVal -= 26;
      }

      encoded = String.fromCharCode(encodedVal);
      output.push(encoded);
    }
    // numbers
    else if (char >= "0" && char <= "9") {
      encodedVal = char.charCodeAt(0) + (rotationFactor % 10);

      if (encodedVal > "9".charCodeAt(0)) {
        encodedVal -= 10;
      }
      encoded = String.fromCharCode(encodedVal);
      output.push(encoded);
    } //symbols
    else {
      output.push(char);
    }
  }
  return output.join("");
}

// These are the tests we use to determine if the solution is correct.
// You can add your own at the bottom.
function printString(str) {
  var out = '["' + str + '"]';
  return out;
}

var test_case_number = 1;

function check(expected, output) {
  var result = expected == output;
  var rightTick = "\u2713";
  var wrongTick = "\u2717";
  if (result) {
    var out = rightTick + " Test #" + test_case_number;
    console.log(out);
  } else {
    var out = "";
    out += wrongTick + " Test #" + test_case_number + ": Expected ";
    out += printString(expected);
    out += " Your output: ";
    out += printString(output);
    console.log(out);
  }
  test_case_number++;
}

var input_1 = "All-convoYs-9-be:Alert1.";
var rotationFactor_1 = 4;
var expected_1 = "Epp-gsrzsCw-3-fi:Epivx5.";
var output_1 = rotationalCipher(input_1, rotationFactor_1);
check(expected_1, output_1);

var input_2 = "abcdZXYzxy-999.@";
var rotationFactor_2 = 200;
var expected_2 = "stuvRPQrpq-999.@";
var output_2 = rotationalCipher(input_2, rotationFactor_2);
check(expected_2, output_2);

// Add your own test cases here
