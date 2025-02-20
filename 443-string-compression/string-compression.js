/**
 * @param {character[]} chars
 * @return {number}
 */
var compress = function(chars) {
    let write = 0;
    let l = 0;

    while (l < chars.length) {
        let r = l;
        while (r < chars.length && chars[r] == chars[l]) {
            r++;
        }
        
        chars[write++] = chars[l];
        
        let count = r - l;
        if (count > 1) {
            let countStr = count.toString();
            for (let c of countStr) {
                chars[write++] = c;
            }
        }
        
        l = r;
    }
    return write;
};