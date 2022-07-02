/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let brackets = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    let stack = [];
    
    for(let i=0; i<s.length; i++) {
        if (brackets[s[i]]) {
            stack.push(brackets[s[i]]);
        }
        else {
            if (stack.pop() !== s[i]) return false;
        }
    }
    return !stack.length;
};
