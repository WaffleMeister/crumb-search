package HackerRank;

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class DPCoins {
    public static long makeChange(int[] coins, int money) {
        
        int lastUsedCoin = 0;
        
        long[][] solvedCoinAmounts = new long[coins.length][money + 1];
       
        return makeChangeMemoized(coins, money, lastUsedCoin, solvedCoinAmounts) ; 
    }
    
    public static long makeChangeMemoized(int[] coins,
                                          int money,
                                          int coinToUse,
                                          long [][] solvedCoinAmounts) {
        if (money == 0) {
            return 1;
        }
        
        if (coinToUse >= coins.length){
        	return 0;
        }
        
        if (solvedCoinAmounts[coinToUse][money] != 0) {
            return solvedCoinAmounts[coinToUse][money];
        }
        
        long changeSum = 0;
        int denomination = coins[coinToUse];
        
        for(int i = 0; i * denomination <= money; i++) {
            changeSum += makeChangeMemoized(coins, money - (i * denomination), coinToUse + 1, solvedCoinAmounts);
        }
        
        solvedCoinAmounts[coinToUse][money] = changeSum;
        return solvedCoinAmounts[coinToUse][money];
    }
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        int coins[] = new int[m];
        for(int coins_i=0; coins_i < m; coins_i++){
            coins[coins_i] = in.nextInt();
        }
        System.out.println(makeChange(coins, n));
    }
}