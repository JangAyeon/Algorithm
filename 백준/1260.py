{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "too many values to unpack (expected 3)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[5], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m n,m,k \u001b[39m=\u001b[39m \u001b[39mmap\u001b[39m(\u001b[39mint\u001b[39m, \u001b[39minput\u001b[39m()\u001b[39m.\u001b[39msplit())\n\u001b[1;32m      2\u001b[0m graph\u001b[39m=\u001b[39m [[\u001b[39m0\u001b[39m]\u001b[39m*\u001b[39m(n\u001b[39m+\u001b[39m\u001b[39m1\u001b[39m) \u001b[39mfor\u001b[39;00m _ \u001b[39min\u001b[39;00m \u001b[39mrange\u001b[39m(n\u001b[39m+\u001b[39m\u001b[39m1\u001b[39m)]\n\u001b[1;32m      3\u001b[0m visited\u001b[39m=\u001b[39m[\u001b[39m0\u001b[39m]\u001b[39m*\u001b[39m(n\u001b[39m+\u001b[39m\u001b[39m1\u001b[39m) \n",
      "\u001b[0;31mValueError\u001b[0m: too many values to unpack (expected 3)"
     ]
    }
   ],
   "source": [
    "n,m,k = map(int, input().split())\n",
    "graph= [[0]*(n+1) for _ in range(n+1)]\n",
    "visited=[0]*(n+1) \n",
    "\n",
    "for _ in range(n):\n",
    "    x,y = map(int, input().split())\n",
    "    graph[x][y]=graph[y][x]=1\n",
    "\n",
    "def dfs(graph, k, visited):\n",
    "    print(\"dfs\")\n",
    "\n",
    "def bfs(graph, k, visited):\n",
    "    print(\"dfs\")\n",
    "\n",
    "dfs(graph, k,visited)\n",
    "bfs(graph, k,visited)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "31f2aee4e71d21fbe5cf8b01ff0e069b9275f58929596ceb00d14d90e3e16cd6"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
