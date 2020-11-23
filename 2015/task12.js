console.log('JSAbacusFramework.io');
const fs = require('fs');

function sumAllEntries(item, without = null, sum = 0) {
    if (Array.isArray(item)) {
        for (const value of item) {
            if (typeof value === 'number') {
                sum += value;
            } else if (Array.isArray(value)) {
                sum = sumAllEntries(value, without, sum);
            } else if (typeof item === 'object') {
                sum = sumAllEntries(value, without, sum);
            }
        }
    } else if (typeof item === 'object') {
        if (Object.values(item).some(v => v === without)) {
            return sum;
        }
        for (const [key, value] of Object.entries(item)) {
            if (typeof value === 'number') {
                sum += value;
            } else if (Array.isArray(value)) {
                sum = sumAllEntries(value, without, sum);
            } else if (typeof item === 'object') {
                sum = sumAllEntries(value, without, sum);
            }
          }
    }

    return sum;
}

try {
    const input = fs.readFileSync('task12Input.txt', 'utf8');
    const jsonData = JSON.parse(input);
    let sum = sumAllEntries(jsonData);
    console.log(sum);

    //part two
    sum = sumAllEntries(jsonData, 'red' );
    console.log(sum);
  
} catch(e) {
    console.log('Error:', e.stack);
}