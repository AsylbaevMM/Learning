package org.example;

public class HashTable<K, V> {
    private class Entity{
        private K key;
        private V value;

    }
    private class Basket{
        private Node head;
        private class Node {
            private Entity value;
            private Node next;
        }
    }
}

