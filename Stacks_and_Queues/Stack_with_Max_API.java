private static class ElementWithCachedMax {
    public Integer element;
    public Integer max;

    public ElementWithCachedMax(Integer element, Integer max) {
        this.element = element;
        this.max = max;
    }
}

public static class Stack {
    // stores element with cached maximum pair.
    private Deque<ElementWithCachedMax> elementWithCachedMax = new LinkedList<>();

    public boolean empy() { 
        return elementWithCachedMax.isEmpty();
    }

    public Integer max() {
        if (empty()) {
            throw new IllegalStateException("max(): Empty stack!")
        }
        return elementWithCachedMax.peek().max;
    }

    public Integer pop() {
        if (empty()) {
            return new IllegalStateException("pop(): Empty stack!")
        }
        return elementWithCachedMax.removeFirst().element;
    }

    public void push(Integer x) {
        elementWithCachedMax.addFirst(
            new ElementWithCachedMax(x, empty() ? x : max())
        );
    }
}

/*
    Optimization: We can improve on the best-case space needed by observing that 
    if an element e being pushed is smaller than the maximum element already
    in the stack, then e can never be the maximum, so we do not need to record it. 
    We cannot store the sequence of maximum values in a separate stack because of 
    the possibility of duplicates. We resolve this by additionally recording 
    the number of occurrences of each maximum value.
*/

// O(1) is the time complexity for each method. 
// The worst-case additional space complexity is 0(n), 
// which occurs when each key pushed is greater than all keys in the primary stack.

private static class MaxWithCount {
    
    public Integer max;
    public Integer count;

    public MaxWithCounts(Integer max, Integer count) {
        this.max = max;
        this.count = count;
    } 
}

public static class Stack {
    private Deque<Integer> element = new LinkedList<>();
    private Deque<MaxWithCount> cachedMaxWithCount = new LinkedList<>();

    public boolean empty() {
        return element.isEmpty();
    }

    public Integer max() {
        if (empty()) {
            return new IllegalStateException("max(): Empty stack!");
        }
        return cachedMaxWithCount.peekFirst().max;
    }

    public Integer pop() {
        if (empty()) {
            return new IllegalStateException("min(): Empty stack!");
        }
        Integer popElement = cachedMaxWithCount.removeFirst();
        if (popElement.equals(cachedMaxWithCount.peekFirst().max)) {
            cachedMaxWithCount.peekFirst().count = cachedMaxWithCount.peekFirst().count - 1;
            if (cachedMaxWithCount.peekFirst().count.equals(0)) {
                cachedMaxWithCount.removeFirst();
            }
        }
        return popElement;
    }

    public void push(Integer x) {
        element.addFirst(x);
        if (!cachedMaxWithCount.isEmpty()) {
            if (Integer.compare(x, cachedMaxWithCount.peekFirst().max) == 0) {
                cachedMaxWithCount.peekFirst().count = cachedMaxWithCount.peekFirst().count + 1;
            } else if (Integer.compare(x, cachedMaxWithCount.peekFirst().max) > 0) {
                cachedMaxWithCount.addFirst(new MaxWithCounts(x, 1));
            }
        } else {
            cachedMaxWithCount.addFirst(new MaxWithCounts(x, 1));
        }
    }
}

/*
    https://leetcode.com/problems/max-stack/solution/
    Leetcode Solutions to same problem.
*/
