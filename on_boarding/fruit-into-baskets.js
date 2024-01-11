/**
 * @param {number[]} fruits
 * @return {number}
 */
var totalFruit = function(tree) {
    let [i,j,max] = [0,0,0];
    class counter {
        constructor() {
            this.map = new Map();
        }
        
        add(k) {
            if(this.map.has(k)) {
                this.map.set(k, this.map.get(k) + 1);
            } else {
                this.map.set(k, 1);
            }
        }
        
        remove(k) {
            const val = this.map.get(k) - 1;
            if(val) {     
                this.map.set(k, val);
            } else {
                this.map.delete(k);
            }
        }
        
        get size() {
            return this.map.size;
        }
        
        get sum() {
            return Array.from(this.map.values()).reduce((c, r) => {return c + r;});
        }
    }
    const count = new counter();
    while(j < tree.length) {
        count.add(tree[j++]);
        while(count.size > 2) {
            count.remove(tree[i++]);
        }
        max = Math.max(max, count.sum);
    }
    return max;
};