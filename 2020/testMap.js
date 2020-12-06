let startInput = 'abcdefg'
let nextInput = 'abcf';
let dict = {};

for (let char of startInput) {
    dict[char] = true;
}
console.log(dict);

for (let char in dict) {
    console.log(char);
    if (nextInput.indexOf(char) == -1) {
     delete dict[char];
    }
 }

 console.log(dict);