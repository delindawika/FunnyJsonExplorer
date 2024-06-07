
## UML Diagram

<img width="727" alt="Screenshot 2024-06-08 at 01 26 59" src="https://github.com/delindawika/FunnyJsonExplorer/assets/65715881/a9b0fad0-ecc8-47bb-9e9e-1ddc11a138fa">

## Design Pattern
Here in our code, we use the **abstract factory design pattern**
### Abstract Factory 1: StyleFactory
This is an abstract base class declaring an interface for creating style products.
- Concrete Factories: TreeFactory and RectangleFactory

  These are concrete classes that implement the StyleFactory interface. Each factory is responsible for creating a specific type of product     (TreeStyle and RectangleStyle, respectively).

- Abstract Product: Style

  This abstract class defines an interface for a type of object. Style has an abstract method draw(container), which needs to be implemented by all concrete products.

- Concrete Products: TreeStyle and RectangleStyle

  These classes implement the Style abstract class and provide specific implementations of the draw(container) method. TreeStyle renders the JSON as a tree structure, and RectangleStyle renders it as a series of indented rectangles.

### Abstract Factory 2: IconFactory
This is an abstract base class declaring an interface for creating icon products.
- Concrete Factories: PokerFaceFactory and MoonSunFactory

  These are concrete classes that implement the IconFactory interface. Each factory is responsible for creating a specific type of product   
- Abstract Product: Branch and Leaf
- Concrete Products: PokerFaceBranch, PokerFaceLeaf, MoonSunBranch, MoonSuneBranch

  These classes implement the Branch and Leaf abstract class and based on the factory, the products that are going to be produced will be different.

### Client (FunnyJsonExplorer)
The client uses interfaces declared by the abstract factory and abstract product to interact with the products. The client is independent of how these products are created, allowing the client code to support different product variants without modification.

## Output
#### Style=Tree style, icon=poker-face
<img width="669" alt="Screenshot 2024-06-08 at 02 02 04" src="https://github.com/delindawika/FunnyJsonExplorer/assets/65715881/ead20793-7289-4cc8-b9d9-b756a44d2956">

#### Style=Tree style, icon=moon-sun
<img width="659" alt="Screenshot 2024-06-08 at 02 02 33" src="https://github.com/delindawika/FunnyJsonExplorer/assets/65715881/80fc7be7-14ae-42d1-aecb-7bdfc9854593">

#### Style=Rectangle style, icon=poker-face
![Screenshot 2024-06-08 at 02 06 31](https://github.com/delindawika/FunnyJsonExplorer/assets/65715881/96d88a71-1d02-4818-8d2c-561fb4954680)

#### Style=Rectangle style, icon=moon-sun
![Screenshot 2024-06-08 at 02 06 31](https://github.com/delindawika/FunnyJsonExplorer/assets/65715881/f04592ee-b815-482c-88aa-3c352ae93199)

## Adding New Style
If you want to add another style other than tree/rectangle, here are the steps that you can follow:
##### 1. Implement your new style concrete product in Style.py. For example, let's name the new style as teststyle
<img width="368" alt="Screenshot 2024-06-08 at 02 29 11" src="https://github.com/delindawika/FunnyJsonExplorer/assets/65715881/eba63399-b5b0-4e34-81a2-163de33b5837">

##### 2. Create your new concrete factory in StyleFactory.py
<img width="434" alt="Screenshot 2024-06-08 at 02 30 50" src="https://github.com/delindawika/FunnyJsonExplorer/assets/65715881/86fd5b23-bbff-4c8a-b0e3-4b7e4bda2037">

##### 3. Call it from the FunnyJsonExplorer's class "show" module in FunnyJsonExplorer.py
<img width="408" alt="Screenshot 2024-06-08 at 02 33 06" src="https://github.com/delindawika/FunnyJsonExplorer/assets/65715881/f984920f-6225-41b3-af70-e520f58c8fbc">

##### 4. Add the style choice inside the parser
<img width="887" alt="Screenshot 2024-06-08 at 02 49 30" src="https://github.com/delindawika/FunnyJsonExplorer/assets/65715881/d0522167-e6ee-4b0a-ba53-1a7809cdc58f">

## Adding New Icon Family
If you want to add another icon family other than poker-face/moon-sun, here are the steps that you can follow:
#### 1. Add our new concrete factory in IconFactory.py and define its branch and leaf symbol. Let's call our new factory as StarDollarFactory.
<img width="426" alt="Screenshot 2024-06-08 at 02 46 46" src="https://github.com/delindawika/FunnyJsonExplorer/assets/65715881/1b6c2110-c2fd-435b-a5da-39012e340e06">

#### 2. Call it from the FunnyJsonExplorer's class "show" module in FunnyJsonExplorer.py
<img width="480" alt="Screenshot 2024-06-08 at 02 48 37" src="https://github.com/delindawika/FunnyJsonExplorer/assets/65715881/e90e89bc-6bad-4690-8aa5-f69f1e55317d">

#### 3. Add the icon family choice inside the parser
<img width="1087" alt="Screenshot 2024-06-08 at 02 49 23" src="https://github.com/delindawika/FunnyJsonExplorer/assets/65715881/bb48e21a-1622-4c42-af2a-7c0a468831b4">

## Implementation Using Other Design Patterns
#### Composite
- Component Interface/Abstract Class

Attributes: Include common attributes such as style and icon.
Methods: Include methods like draw(), add(Component), remove(Component), and accessor methods for style and icon (e.g., getStyle(), setIcon()).

- Leaf Class
  
This class implements or extends the Component class. It will use the style and icon attributes defined in Component for its drawing operations or other functionality. Since leaves represent the end objects in a composition, they will typically implement the drawing behavior (draw()) using their specific styles and icons.

- Composite Class
  
The composite class also implements or extends the Component. It will manage a collection of Component objects and can propagate style and icon settings to its children if such propagation is needed.

#### Builder
To incorporate the Builder design pattern into the existing UML for the FunnyJsonExplorer project, we can follow these modifications:
- Builder Interface: Defines methods to construct Container parts step-by-step, such as buildContainer(), buildStyle(), and buildIcon().
- Concrete Builders: Implement the Builder interface with classes like SimpleContainerBuilder and ComplexContainerBuilder to construct and assemble parts of the Container in various configurations.
- Director Class: Utilizes a Builder to orchestrate the construction of the Container through the construct() method.
- Client Class: Interacts with the Director and ConcreteBuilders to initiate object creation
