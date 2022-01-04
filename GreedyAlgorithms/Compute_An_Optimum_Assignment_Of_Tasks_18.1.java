class Compute_An_Optimum_Assignment_Of_Tasks {
    private static class PairedTasks {
        public Integer task1;
        public Integer task2;

        public PairedTasks(Integer task1, Integer task2) {
            this.task1 = task1;
            this.task2 = task2;
        }
    }

    public static List<PairedTasks> optimumTaskAssingment(List<Integer> taskDurations) {
        Collections.sort(taskDurations);
        List<PairedTasks> optimumAssignments = new ArrayList<>();
        for(int i = 0, j = taskDurations.size()-1; i < j; i++, j--) {
            optimumAssignments.add(new PairedTasks(taskDurations.get(i), taskDurations.get(j)));
        }

        return optimumAssignments;
    }
}

// time complexity is dominated by the sorting.     