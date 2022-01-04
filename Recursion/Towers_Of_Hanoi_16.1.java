private static final int NUM_PEGS = 3;

public static void computeTowerHanoi(int numRings) {
    List<Deque<Integer>> pegs = new ArrayList<>();
    for (int i = 0; i < NUM_PEGS; i++) {
        pegs.add(new LinkedList<Integer>());
    }

    for (int i = numRings; i >= 1; i--){
        pegs.get(0).addFirst(i);
    }

    computeTowerHanoiSteps(numRings, pegs, 0, 1, 2);
}

private static void computeTowerHanoiSteps(int numRingsToMove, List<Deque<Integer>> pegs, int fromPeg, int toPeg, int usePeg) {
    if (numRingsToMove > 0) {
        computeTowerHanoiSteps(numRingsToMove - 1, pegs, fromPeg, usePeg, toPeg);
        pegs.get(toPeg).addFirst(pegs.get(fromPeg).removeFirst());
        System.out.println("Move from peg " + fromPeg + " to peg " + toPeg);
        computeTowerHanoiSteps(numRingsToMove - 1, pegs, usePeg, toPeg, fromPeg);
    }
}

// Better explanation.
// https://www.youtube.com/watch?v=rf6uf3jNjbo

// The number of moves, T(n), satisfies the following recurrence: 
// T(n) = T(n —1) + 1 + T(n —1) =1 + 2T(n - 1). The first T(n - 1) corresponds to the transfer of the top n —1
// rings from PI to P3, and the second T(n - 1) corresponds to the transfer from P3 to P2. This recurrence solves to T(n) = 2" —1. 
// One way to see this is to "unwrap" the recurrence: 
// T(n) = 1 + 2 + 4H 1- 2kT(n - k). 
// Printing a single move takes 0(1) time, so the time complexity is 0(2").



// Another solution 
// n : Number of plates
// Origin: 1st tower, Buffer: Tower that will be used as buffer , Destination: Tower on which all plates has to transferred.
void moveTowers(int n, Tower destination, Tower buffer) {
       if(n>0) {
	      moveTowers(n-1, buffer, destination);
		  moveTopElement(destination);
		  moveTowers(n-1, destination, origin)
	   }
}
// This is a method in Tower class
 void moveTopTo(Tower t) { 
         int top= disks.pop(); 
         t.add(top);
 }