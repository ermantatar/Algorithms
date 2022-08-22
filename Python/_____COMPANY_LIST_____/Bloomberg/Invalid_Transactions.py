
"""
Algo: 
    Create a hash table around this structure 
    "time" => 
            "name" = set( [cityA, cityB..] )

    time 0'da Erman sent 60 dollars, then time 10 Erman sent 30 dollars, if both from the same city no problem, if not, both are invalid transactions.
"""

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        def split_transaction(trans):
            name, time, amount, city = trans.split(',')
            return name, int(time), int(amount), city
        
        def create_transaction_store():
            prev_trans = defaultdict(lambda: defaultdict(set))
            for trans in transactions:
                name, time, amount, city = split_transaction(trans)
                prev_trans[time][name].add(city)
            return prev_trans

        
        
        def is_invalid(trans):
            name, time, amount, city = split_transaction(trans)
            
            if amount > 1000:
                return True
            
            for t in range(time - 60, time + 61):
                if t not in prev_trans: 
                    continue 
                if name not in prev_trans[t]: 
                    continue 
                # if this city is not even there in the my list 
                if city not in prev_trans[t][name]:
                    return True
                # if there is more city than this city, red flag
                if len(prev_trans[t][name]) > 1:
                    return True 
        
        
        
        invalid = []
        
        prev_trans = create_transaction_store()
        
        for trans in transactions:
            if is_invalid(trans):
                invalid.append(trans)
        
        return invalid 