import java.util.List;
import java.util.ArrayList;

public class Generics {
    public static void main(String[] args) {
        List l = new ArrayList();
        l.add(42);
        l.add("CS339");
        int n = (int) l.get(0);

        Stack<Integer> intStack = new Stack<>();
        intStack.push(10);
        intStack.push(20);
        System.out.println("STACK: " + intStack);
        System.out.println(intStack.pop());

        Stack<String> strStack = new Stack<>();
        strStack.push("CS339");
        strStack.push("CS355");
        System.out.println(strStack.top());
    }
}

class Stack<T> {
    List<T> elems = new ArrayList<>();
    void push(T e) {
        elems.add(e);
    }
    T top() {
        return elems.get(elems.size() - 1);
    }
    T pop() {
        return elems.remove(elems.size() - 1);
    }
    public String toString() {
        String s = "";
        for (T e : elems) {
            s += e + " ";
        }
        return s;
    }
}
