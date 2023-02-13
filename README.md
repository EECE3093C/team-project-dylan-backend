# Writing on GitHub Assignment

Software engineers need to be able to communicate technical information effectively to various stakeholders, including team members, clients, and management. Technical writing enables us to present complex information in a clear and concise manner, ensuring that everyone has a comprehensive understanding of the software being developed. This helps to avoid misunderstandings, delays, and other problems that can arise when technical information is not communicated effectively.

This assignment is a simple introduction to writing on GitHub using **Markdown[^1]**. GitHub has its own flavor of Markdown, so you must follow their syntax. Please see the [“Writing on GitHub”](https://docs.github.com/en/get-started/writing-on-github) documentation published by GitHub for more details on their Markdown syntax.

### Fenced Code Blocks

You can create fenced code blocks by placing triple backticks ``` before and after the code block. Syntax highlighting in your fenced code block is enabled by adding an optional language identifier. For example, to syntax highlight Python code your fenced code block would begin with ``Python

```Python

  class Circle():
      def __init__(self, r):
           self.radiuis = r
           
      def area(self):
           return self.radius**2*3.14
           
      def perimeter(self):
           return 2*self.radius*3.14 
 ```

### Mathematical Expressions

 GitHub supports LaTeX formatted math within Markdown, it uses the corss-browser JavaScript library MathJax for rendering. Here is a mathematical expression for Binomial
 coefficients:

$$
\  \binom{n}{k} = \frac{n!}{k!(n-k)!}  \
$$

[^1]: [GitHub Flavored Markdown Spec](https://github.github.com/gfm/)

### Diagams

You can create diagrams in Markdown using four different syntaxes: mermaid, geoJSON and topoJSON, and ASCII STL. Similar to fenced code blocks, digrams are rendered by placing triple backticks ``` before and after the diagram code block, but you must specify a syntax identifer (e.g., mermaid) after initial backticks. Here is an example of a class diagram defined through the mermaid[^2] syntax.

```mermaid

classDiagram
    Animal <|-- Duck
    Animal <|-- Fish
    Animal <|-- Zebra
    Animal : +int age
    Animal : +String gender
    Animal: +isMammal()
    Animal: +mate()
    class Duck{
        +String beakColor
        +swim()
        +quack()
    }
    class Fish{
        -int sizeInFeet
        -canEat()
    }
    class Zebra{
        +bool is_wild
        +run()
    }
```

And here is a sequence diagram:

[^2]: [Marmaid diagramming and charting tool](https://mermaid.js.org/)

```mermaid
     sequenceDiagram
        Alice->>John: Hello John, how are you?
        John-->>Alice: Great!
        Alice-)John: See you later!
```
