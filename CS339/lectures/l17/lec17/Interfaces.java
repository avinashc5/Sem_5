import java.util.List;
import java.util.ArrayList;

interface Drawable {
    void draw();
}

abstract class Shape {
    abstract double area();
}

class Circle extends Shape implements Drawable {
    double r;
    Circle(double r) {
        this.r = r;
    }
    public void draw() {
        System.out.println("Drawing Circle with radius " + r);
    }
    double area() { return Math.PI * r * r; }
}

class Rectangle extends Shape implements Drawable {
    int width, height;
    Rectangle(int w, int h) {
        this.width = w; this.height = h;
    }
    public void draw() {
        System.out.println("Drawing Rectangle with width " + width + " and height " + height);
    }
    double area() { return width * height; }
}

enum Color { RED, BLUE, GREEN; }

abstract class UIElement {
    Color color;
    UIElement() {
        color = Color.RED;
    }
}

class Button extends UIElement implements Drawable {
    public void draw() {
        System.out.println("Drawing Button with color " + color);
    }
    void click() {
        System.out.println("Button clicked!");
    }
}

public class Interfaces {
    public static void main(String[] args) {
        List<Drawable> items = new ArrayList<>();
        items.add(new Circle(5));
        items.add(new Rectangle(3, 4));
        items.add(new Button());
        for (Drawable d : items) {
            d.draw();
        }
    }
}