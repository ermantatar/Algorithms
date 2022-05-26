public static class Star implements Comparable<Start> {

    private double x, y, z;

    public Star(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public double distance() { 
        return Math.sqrt(x * x + y * y + z * z); 
    }

    @Override
    public int compareTo(Star secondStar) {
        return Double.compare(this.distance(), secondStar.distance());
    }

    public static List<Star> findClosestKStars(int k, Iterator<Star> stars) {
        // maxHead to store the closest k stars seen so far.
        PriorityQueue<Star> maxHeap = new PriorityQueue<>(k, Collections.reverseOrder());

        while(stars.hasNext()) {
            // add each star into maxHeap, when the size reached the k+1, remove the max distance. 
            Star star = stars.next();
            maxHeap.add(star);
            if (maxHeap.size() == k + 1) {
                maxHeap.remove();
            }
        }

        List<Star> orderedStars = new ArrayList<Start>(maxHeap);
        // the only guarentee PriorityQueue makes about ordering is that the 
        // maximum element comes first, so we orderedStars

        Collections.sort(orderedStars);
        return orderedStars;
    }
    
}