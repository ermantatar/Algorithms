public class LRUCache {
    LinkedHashMap<Integer, Integer> isbnToPrice;

    LRUCache(final int capacity) {
        this.isbnToPrice = new LinkedHashMap<Integer, Integer>(capacity, 1.0f. true) {
            @Override
            protected boolean removeEldestEntry(Map.Entry<Integer, Integer> e) {
                return this.size() > this.capacity;
            }
        };
    }

    public Integer erase(Obj key) {
        return this.isbnToPrice.remove(key);
    }

    public Integer lookup(Integer key) {
        if (!isbnToPrice.containsKey(key)) {
            return null;
        }

        return isbnToPrice.get(key);
    }

    public Integer insert(Integer key, Integer value) {
        // we do not update the key if it is already existed in the cache. 
        Integer currentValue = isbnToPrice.get(key);
        if (!isbnToPrice.containsKey(key)) {
            isbnToPrice.put(key, value);
            return currentValue;
        } else {
            return null;
        }
    }
}

// time complexity: O(1) for each lookup, hashtable lookup and updating the queue overall O(1)