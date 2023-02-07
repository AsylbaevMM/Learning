package org.example;

import java.util.LinkedList;
import java.util.Queue;

class node
{
    int x, y, distance;

    node(int x, int y, int dist)
    {
        this.x = x;
        this.y = y;
        this.distance = dist;
    }
}

public class Main
{
    // это должна быть длина строки и столбца введенной матрицы
    static int M = 8;
    static int N = 11;

    static boolean isValid(int[][] mat, boolean[][] visited, int row, int col)
    {
        return ((row >= 0) && (row < M)) && ((col >= 0) && (col < N)) && (mat[row][col] == 1) && (!visited[row][col]);
    }

    private static void bfs(int[][] matrix, int i, int j, int x, int y)
    {
        int[] row =
                { -1, 0, 0, 1 };
        int[] col =
                { 0, -1, 1, 0 };

        boolean[][] visited = new boolean[M][N];
        Queue<node> q = new LinkedList<node>();
        visited[i][j] = true;
        q.add(new node(i, j, 0));
        int minimum_distance = Integer.MAX_VALUE;
        while (!q.isEmpty())
        {
            node node = q.poll();
            i = node.x;
            j = node.y;
            int dist = node.distance;
            if (i == x && j == y)
            {
                minimum_distance = dist;
                break;
            }

            for (int k = 0; k < 4; k++)
            {
                if (isValid(matrix, visited, i + row[k], j + col[k]))
                {
                    visited[i + row[k]][j + col[k]] = true;
                    node n = new node(i + row[k], j + col[k], dist + 1);
                    q.add(n);
                }
            }
        }

        if (minimum_distance == Integer.MAX_VALUE)
        {
            System.out.print("Не удается достичь места назначения");
        }
        else
        {
            System.out.print("Кратчайший путь имеет длину" + minimum_distance);
        }
    }

    public static void main(String[] args)
    {
        int[][] matrix =
                {
                        { 0, 0, 0, 0, 0, 0, 0, 0 },
                        { 0, 0, -1, 0, 0, 0, 0, 0 },
                        { 0, 0, -1, 0, -1, 0, -1, 0 },
                        { 0, 0, -1, 0, 0, 0, -1, 0 },
                        { 0, 0, -1, 0, 0, 0, -1, 0 },
                        { 0, -1, -1, -1, -1, -1, -1, 0 },
                        { 0, 0, -1, 0, 0, 0, -1, 0 },
                        { 0, 0, -1, 0, 0, 0, -1, 0 },
                        { 0, 0, 0, 0, 0, 0, -1, 0 },
                        { 0, 0, 0, 0, 0, 0, -1, 0 },
                        { 0, 0, 0, 0, 0, 0, 0, 0 } };
        bfs(matrix, 0, 0, 8, 11);
    }
}