"""this program to find the number of repeat sub_string in the string"""

def count_substring(string, sub_string):
    count = 0
    s = string
    sb = sub_string
    for i in range (len(s)-len(sb) + 1):
        if s[i:i+len(sb)]==sb:
            count+=1
            
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)