<-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->

Binary search is an efficient algorithm for finding an item from a sorted list of items. 
It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one.

<-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->

Set the search space equal to the sorted array
    
Take the middle element of the search space and compare it to the target value.
    - If the target equals the middle element, you have found the target value. Return the index of the middle element and terminate the function.
    - If the target is smaller than the middle element, halve the search space by discarding all elements to the right of the middle element and continue the search on its left side because the array is sorted in ascending order. 
    - If the target is greater than the middle element, halve the search space by discarding all elements to the left of the middle element and continue the search on its right side because the array is sorted in ascending order.
Repeat this step until the target is found.

<-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->
