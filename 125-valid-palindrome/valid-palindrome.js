/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let deleteSymbolS = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
    let l = 0;
    let r = deleteSymbolS.length - 1;

    while (l < r) {
        if (deleteSymbolS[l] !== deleteSymbolS[r]) {
            return false;
        }
        l++;
        r--;
    }
    return true;
};