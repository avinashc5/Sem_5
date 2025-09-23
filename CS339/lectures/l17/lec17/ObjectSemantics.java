public class ObjectSemantics {
    public static void main(String[] args) {
        Animal p1;
//        p1 = new Animal();
//        System.out.println(p1.x + " " + p1.y);
        Animal p2;
        p2 = new Monkey();
//        System.out.println(p2.x + " " + p2.y + " " + ((Monkey) p2).y + " " + ((Monkey) p2).z);
        p2.sound();
        p2.tail();
        ((Animal) p2).tail();

        System.out.println(p2.y + " " + ((Monkey) p2).y);
        System.out.println("Getter: " + p2.getY());

        Monkey p3 = new Monkey();
        System.out.println(p3.y + " " + ((Animal) p3).y);
    }
}

class Animal {
    int x;
    int y;
    Animal() {
        x = y = 10;
    }
    int getY() {
        return y;
    }
    void sound() {
        System.out.println("Animal's sound: " + y);
    }
    void tail() {
        System.out.println("Animal's tail");
    }
}

class Monkey extends Animal {
    int y;
    int z;
    Monkey() {
        //super();
        x = 20;
        y = 20;
        z = 20;
    }
    int getY() {
        return y;
    }
    void tail() {
        System.out.println("Monkey's tail");
    }
}
