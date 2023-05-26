package org.example;

public class LinkedList {
    private Node head;
    private Node tail;

    private class Node {
        private Node next;
        private Node previous;
        private int value;
    }

    public void addFirst(int value) {
        Node node = new Node();
        node.value = value;
        if (head != null) {
            node.next = head;
        } else {
            tail = node;
        }
        node.previous = null;
        head = node;
    }

    public void dellFirst(int value) {
        if (head != null) {
            head = head.next;
        }
        head.previous = null;
    }


}
