// ((Greg,14), (John,12), (Andy,11), (Jim,13), (Phil,12), (Bob,13), (Chip,13), (Tim,14)). 
// ((Greg,14),_,(John,12),_,(Andy,11),(Jim,13),_,_)


public static class Person {
    public Integer age;
    public String name;

    public Person(Integer age, String name) {
        this.age = age;
        this.name = name;
    }
}

public static void groupByAge(List<Person> people) {
    Map<Integer, Integer> ageToCount = new HashMap<>();
    for(Person p : people) {
        if (ageToCount.containsKey(p.age)) {
            ageToCount.put(p.age, ageToCount.get(p.age) + 1);
        } else {
            ageToCount.put(p.age, 1);
        }
    }

    Map<Integer, Integer> ageToOffset = new HashMap<>();
    int offset = 0;
    for (Map.Entry<Integer, Integer> ac : ageToCount.entrySet()) {
        ageToOffset.put(ac.getKey(), offset);
        offset += ac.getValue();
    }

    while(!ageToOffset.isEmpty()) {
        Map.Entry<Integer, Integer> from = ageToOffset.entrySet().iterator().next();
        Integer toAge = people.get(from.getValue()).age;
        Integer toValue = ageToOffset.get(toAge);

        Collections.swap(people, from.getValue(), toValue);
        Integer count = ageToCount.get(toAge) - 1;
        ageToCount.put(toAge, count);
        if (count > 0) {
            ageToOffset.put(toAge, toValue + 1);
        } else {
            ageToOffset.remove(toAge);
        }
    }
}

// _,Alex,_,_
// Mark,Alex,_,_

// Forward index to backward locating technique. 

/*
The time complexity is 0(n), since the first pass entails n hash table inserts, 
and the second pass spends O(1) time to move one element to its proper location. 
The additional space complexity is dictated by the hash table, i.e., 
O(m), where m is the number of distinct ages.
*/