import {LinkedListNode, createLinkedList, toList} from './LinkedList.js'


let merge2Country = function(head1, head2) {
    // if both lists are empty then merged list is also empty
    // if one of the lists is empty then other is the merged list
    if (!head1) {
      return head2;
    } else if (!head2) {
      return head1;
    }

    let mergedHead = null;
    if (head1.data <= head2.data) {
      mergedHead = head1;
      head1 = head1.next;
    } else {
      mergedHead = head2;
      head2 = head2.next;
    }

    let curr = mergedHead;

    while (head1 && head2) {
      let temp = null;
      if (head1.data <= head2.data) {
        temp = head1;
        head1 = head1.next;
      } else {
        temp = head2;
        head2 = head2.next;
      }
      curr.next = temp;
      curr = temp;
    }
    if (head1) {
      curr.next = head1;
    } else if (head2) {
      curr.next = head2;
    }

    return mergedHead;
};

function mergeKCounty(lists){ // Main function

    if (lists.length > 0){
        res = lists[0];
        for (var i = 1; i < lists.length; i++) {
            res = merge2Country(res, lists[i]);
        }
        return res;
    }
}