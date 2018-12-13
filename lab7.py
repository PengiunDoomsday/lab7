"""
Created on Fri Dec 7 21:04:34 2018

@author: Javier Soon
ID:      80436654
Professor: Diego Aguirre
T.A.:      Manoj Saha

Description: Compare two words in which it would count the number of operations
needed to make either word be the same to the other.
"""



def edit_distance(word1, word2):
    ''' method takes two words, and returns the edit distance of the words '''
    str1 = len(word1) + 1     # increases the size of the word by 1 for the "space"
    str2 = len(word2) + 1

    matrix = {}     # creates a dictionary 
    
    for i in range(str1): 
        matrix[i,0] = i       # makes the matrix work like this matrix[i][0]
        
    for j in range(str2): 
        matrix[0,j] = j
        
    for i in range(1, str1):
        for j in range(1, str2):
            if word1[i - 1] == word2[j - 1]:        # if the char at the position are the same = 0
                cost = 0
            else:
                cost = 1        # if the char at the position are different cost = 1
            matrix[i,j] = min(matrix[i, j-1]+1, matrix[i-1, j]+1, matrix[i-1, j-1]+cost)
                # looks at the surrounding three positions, finds the min and adds the cost which is either a 1 or 0
                # depending if they the same or not.

    return matrix[i,j]




def main():
    word1 = "doing"
    word2 = "hellos"
    
    distance = edit_distance(word1, word2)
    print(distance)
    
main()