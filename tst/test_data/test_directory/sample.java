package HackerRank;
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Tries {

	private Node root;
    
    public Tries(){
        this.root = new Node();
    }
    
    public void addString(String s){
        root.addChar(s, 0);
    }
    
    public int lookUp(String prefix) {
        return root.lookupPrefix(prefix, 0);
    }
    
    private class Node {
        int wordCount;
        HashMap<Character, Node> children;

        public Node(){
        	wordCount = 0;
            children = new HashMap<Character, Node>();
        }
        
        public void addChar(String input, int idx){
            if (idx >= input.length()){
                return;
            }
            
            char charToAdd = input.charAt(idx);
            Node child = children.get(charToAdd);
   
            if (child == null){
                child = new Node();
                children.put(charToAdd, child);
            }
            
            child.wordCount++;
            child.addChar(input, idx + 1);
        }
    
        public int lookupPrefix(String prefix, int idx){
            char charToFind = prefix.charAt(idx);
            Node child = children.get(charToFind);

            if (child == null){
                return 0;
            } else {
                if (idx == prefix.length() - 1){
                    return child.wordCount;
                } else {
                    return child.lookupPrefix(prefix, idx + 1);
                }
                
            }
        }
    }
    
    public static void main(String[] args) {
        

        Tries s = new Tries();
        
        s.addString("s");
        s.addString("ss");
        s.addString("sss");

        System.out.println(s.lookUp("s"));
        System.out.println(s.lookUp("ss"));
        System.out.println(s.lookUp("sss"));
        System.out.println(s.lookUp("ssss"));
 
    }
}

