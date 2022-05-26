// Array Based Desin

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */

// time complexity: O(1). All of the methods in our circular data structure is of constant time complexity.
// space complexity: O(N)
// The overall space complexity of the data structure is linear, where N is the pre-assigned capacity of the queue. 
// However, it is worth mentioning that the memory consumption of the data structure remains as its pre-assigned capacity during its entire life cycle.
class MyCircularQueue {
    
    private int[] queue;
    private int headIndex;
    private int count;
    private int capacity;

    public MyCircularQueue(int k) {
        this.capacity = k;
        this.queue = new int[k];
        this.headIndex = 0;
        this.count = 0;
    }
    
    /* Insert an element into the circular queue. Return true if the operation is successful. */
    public boolean enQueue(int value) {
        if (this.count == this.capacity) {
            return false;
        }
        this.queue[ (this.headIndex + this.count) % this.capacity ] = value;
        this.count += 1;
        return true;
    }
    
    /** Delete an element from the circular queue. Return true if the operation is successful. */
    public boolean deQueue() {
        if (this.count == 0) {
            return false;
        }
        this.headIndex = (this.headIndex + 1) % capacity; // we are removing from the head
        this.count -= 1;
        return false;
    }
    
    public int Front() {
        if (this.count == 0) {
            return -1;
        }
        return this.queue[this.headIndex];
    }
    
    public int Rear() {
        if (this.count == 0) {
            return -1;
        }
        int tailIndex = (this.headIndex + this.count - 1) % capacity;
        return this.queue[tailIndex];
    }
    
    public boolean isEmpty() {
        return (this.count == 0);
    }
    
    public boolean isFull() {   
        return (this.count == this.capacity);
    }
}




// Linked List Solution 

// time complexity: O(1)
// space complexity: The upper bound of the memory consumption for our circular queue would be O(N), same as the Array approach. However, it should be more memory efficient as we discussed in the intuition section.

class Node {
    public int value;
    public Node nextNode;
    
    public Node(int value) {
        this.value = value;
        this.nextNode = null;
    }
}


class MyCircularQueue {
    
    private Node head, tail;
    private int count;
    private int capacity;
    
    public MyCircularQueue(int k) {
        this.capacity = k;
    }
    
    public boolean enQueue(int value) {
        if (this.count == this.capacity) {
            return false;
        }
        
        Node newNode = new Node(value);
        if (this.count == 0) {
            head = tail = newNode;
        } else {
            tail.nextNode = newNode;
            tail = newNode;
        }
        
        this.count += 1;
        return true;
    }
    
    public boolean deQueue() {
        if (this.count == 0) {
            return false;
        }
        
        this.head = this.head.nextNode;
        this.count -= 1;
        return true;
    }
    
    public int Front() {
        if (this.count == 0)
            return -1;
        else
            return this.head.value;
    }
    
    public int Rear() {
        if (this.count == 0)
            return -1;
        else
            return this.tail.value;
    }
    
    public boolean isEmpty() {
        return (this.count == 0);
    }

    
    public boolean isFull() {
        return (this.count == this.capacity);
    }
}





// One problem with the above implementation, it is not a thread safe! Our data structure can be corrupted by multi-threaded scenario. 
// https://leetcode.com/problems/design-circular-queue/solution/

// Solution, lets take enqueue func as an example;

class MyCircularQueue {
    
    private Node head, tail;
    private int count;
    private int capacity;
    // Additional variable to secure the access of our queue
    private ReentrantLock queueLock = new ReentrantLock();
    
    public MyCircularQueue(int k) {
        this.capacity = k;
    }
    
    public boolean enQueue(int value) {
        // ensure the exclusive access for the following block.
        queueLock.lock();
        try { 
            if (this.capacity == this.count) {
                return false;
            }
            
            Node newNode = new Node(value);
            if (this.count == 0) {
                head = tail = newNode;
            } else {
                tail.nextNode = newNode;
                tail = newNode;
            }
            this.count += 1;
            
        } finally {
            queueLock.unlock();
        }
        
        return true;
    }
}



