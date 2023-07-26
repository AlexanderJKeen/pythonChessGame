# Ada Chess Project written in Python

# Challenge Outline

### A. Summary and review of the proplem.

    I am creating a Chess Game using Python as the programming language, 
    I will be building a stardard version focusing on creating a simple 
    version of Chess that will acknowledge when a player is in checkmate 
    or that both players are in a stalemate. I will be trying to incorperate 
    as many of the best coding practices. The original release and submitted 
    version will involve a menu that allows you to select a new game. 
    In future releases, player vs computer functionality will be implemented 
    as well as more unique, unkniwn rules such as the 'En Passant' and 'Casteling'. 
    I would also be improving the algoryths so the program may be able to think more 
    than one step ahead to show the user the best moves as opposed to all possible moves.

### B.  UML style diagram illustrating initial overall solution.

### UML : 
![UML](assets/technical_diagrams.jpg)

### C. Initial working plan, overall approach, development strategy and approach to quality

    When I began to design the Chess Game I started with a very basic idea of what a 
    game should look like and as can be seen by my commits I had many trial and errors. 
    when decideing or an approach that would better structure the game I decided to use 
    MVC, Model, View and Controller. This better organises the code and make it easier to 
    make changes and updates and helps to create clean code with better organisation. The 
    view handle the the graphical display such as the the highlighted moves as well as 
    loading the images of the pieces. The model contains the the main methods such as the 
    the games working out all possible moves, the method that works out if a square is under 
    attack and if the potential move is into a valid square. Finally the Controller contains
    the the "control logic" it takes the users choice and then sends it to the model and 
    then waits for the response to send back to the view e.g after a player moves into a 
    checkmate position the response from the model will inform the view that the user has 
    indeed created a checkmate.
        
    My initial plan was to create a file that would take advantage of the libary pygame to 
    draw the board and load the images. I decided that I would try and split the chess logic 
    and graphics in seperate folders as to keep them seperate and less conviluted than a one 
    file project. I was following the kamban board I created quite ridgedly at first however 
    due to my lack of focus on design I began to create two files that became more and more 
    convulted due to the lack of a design approach.

    I attempted to use an agile approach and wanted to create the game in sprints, this however 
    started to become unreasonable due to the time constraint and so created mini sprints in the 
    form of user stories. I also tries to work in the 'red', 'green', 'refactor' style however 
    I amended it to 'code', 'refactor'. This was mainly due to the fact that I was testing the 
    game through user testing and print(). as opposed to writting tests that fail, writting the 
    logic to make them pass and then refactoring that code. Combining both would have been a 
    much better approach and it is deffinantly something I would consider in future., 
    I will disscuss this in more detail below.

### Analysis and decomposition of the overall problem into key ‘epic’ style tasks

    I used the website Trello to plan the user stories out. I didn't plan an epic story within the 
    Trello board as I was working on this as a solo project and overlooked this detail. Reflecting on
    this I would deffinatly wirte the epic story down as if I were to move forward with this project 
    in the months to come I might remember the exact context in which I was planning out this game i.e
    did I want a highly sophisticated chess game or whether it should be more of a simple game. I still 
    have tickets in the 'TODO' list as I have more ideas on how to improve the code as well as add more
    features to the game and I will explain this furthur in a later section. 

![TrelloTicket](assets/trelloticket.png)

![TrelloBoard](assets/trelloboard.png)