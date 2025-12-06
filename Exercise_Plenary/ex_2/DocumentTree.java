import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Stack;
import java.util.stream.Collectors;

class DocumentNode {
    ArrayList<DocumentNode> children;
    ArrayList<DocumentNode> lines;
    String header;
    DocumentNode parent;
    int level;
    int len;

    DocumentNode() {
        children = new ArrayList<>();
        lines = new ArrayList<>();
    }

    DocumentNode(String line) {
        children = new ArrayList<>();
        lines = new ArrayList<>();
        header = line.replaceFirst("#+ ", "");
        level = levelOf(line);
        len = 1;
    }

    int levelOf(String headerString) {
        for (int i = 0; i < headerString.length(); i++) {
            if (headerString.charAt(i) != "#") {
                return i;
            }
        }
        return -1;
    }

    DocumentNode addContent(Stack<String> lines) {
        while (!lines.isEmpty()) {
            String line = lines.peek();
            if (!line.startsWith("#")) {
                this.lines.add(lines.pop());
                len++;
                continue;
            }
            if (levelOf(line) <= level) {
                return this;
            }
            DocumentNode child = new DocumentNode(lines.pop());
            child.parent = this;
            child.addContent(lines);
            children.add(child);
        }
        return this;
    }

    void printTOC() {
        System.out.print(header.indent(level));
        // Pre-order traversal, printing chapter and sub titles
        for (DocumentNode child : children) {
            child.printTOC();

        }
    }

}

class DocumentTree {
    DocumentNode root;

    DocumentTree(Stack<String> lines) {
        root = new DocumentNode();
        root.addContent(lines);
    }

    void printTOC() {
        // e.g.: chapter 1
        for (DocumentNode chapter : root.children) {
            chapter.printTOC();
        }
        /*
         * void printTOC() {
         * // e.g.: chapter 1
         * for (DocumentNode child : root.children) {
         * child.printTOC();
         * // e.g.: chapter 1.1
         * for (DocumentNode child2 : root.children) {
         * child2.printTOC();
         * }
         * }
         * }
         */
    }
}

class Main {
    public static void main(String[] args) {
        Stack<String> lines = new BufferedReader(new InputStreamReader(System.in)).lines()
                .collect(Collectors.toCollection(Stack::new));
        /*
         * // By running cat sicp.md | java Main we get: #Description ... until the
         * first
         * // part of the three until its child node written as ##undertitle is reached.
         * // That is done with this command:
         * System.out.println(args[0]);
         *
         * // The last line of the sicp.md file is given by:
         * System.out.println(lines[lines.length - 1]);
         *
         * // By runnig this loop, we print out all the chapter titles
         * for (String line : lines) {
         * if (line.startsWith("#"))
         * System.out.println(line);
         * }
         */

        Collections.reverse(lines);
        // System.out.println(lines.pop());

        DocumentTree doc = new DocumentTree(lines);
        doc.printTOC();
    }
}
