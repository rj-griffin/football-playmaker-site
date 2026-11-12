from drafter import *
from dataclasses import dataclass

# ==================================================
# WEBSITE DESIGN
# ==================================================

set_website_title("Football Playbook Organizer")
set_site_information( author="RJ Griffin", description="Create and organize American football plays", sources="Thanks to the Drafter docs and my LLM", planning=["C:/Users/rgrif/Downloads/R.J Griffin - CS1 Final Project 1_ Design.pdf", "C:/Users/rgrif/Downloads/RJ Griffin - CS1 Final Project 0_ Pick a Problem.pdf"], links=["https://github.com/rj-griffin/football-playmaker-site"] )

add_website_css("""
    #drafter-body-- {
        font-family: Arial, sans-serif;
    }

    #drafter-body-- h1 {
        color: #F5F0E1;
        letter-spacing: 1px;
    }

    #drafter-body-- h2 {
        color: #9AE6B4;
        margin-top: 22px;
        border-bottom: 1px solid #47715E;
        padding-bottom: 7px;
    }

    #drafter-body-- h3 {
        color: #F5F0E1;
    }

    #drafter-body-- p {
        line-height: 1.6;
    }

    /* Ivory buttons */
    #drafter-body-- button,
    #drafter-body-- input[type="submit"] {
        background-color: #F5F0E1 !important;
        color: #17382D !important;
        border: 2px solid #D8CEB5 !important;
        border-radius: 8px !important;
        padding: 10px 18px !important;
        font-weight: bold !important;
        margin: 5px !important;
        cursor: pointer;
    }

    /* Button hover effect */
    #drafter-body-- button:hover,
    #drafter-body-- input[type="submit"]:hover {
        background-color: #E8DFC8 !important;
        color: #102B24 !important;
        border-color: #C7B995 !important;
    }

    /* Page banner */
    .page-banner {
        background-color: #102B24;
        color: white;
        padding: 22px;
        border-radius: 12px;
        border-bottom: 4px solid #38A169;
        margin-bottom: 18px;
    }

    .page-banner h1 {
        color: #FFFFFF !important;
    }

    .subtitle {
        color: #D1E7DC;
    }

    /* Information cards */
    .info-card {
        background-color: #203B33;
        color: #F0FFF4;
        border: 1px solid #47715E;
        border-radius: 10px;
        padding: 16px;
        margin: 12px 0;
    }

    /* Individual play cards */
    .play-card {
        background-color: #263B35;
        color: white;
        border-left: 5px solid #48BB78;
        border-radius: 8px;
        padding: 14px;
        margin: 12px 0;
    }

    /* Form labels */
    .field-label {
        color: #9AE6B4;
        font-weight: bold;
        margin-top: 12px;
    }

    /* Success and status messages */
    .notice {
        background-color: #214B37;
        color: #C6F6D5;
        padding: 12px;
        border-radius: 8px;
        margin: 10px 0;
    }

    /* Navigation area */
    .navigation {
        background-color: #172C25;
        padding: 12px;
        border-radius: 10px;
        margin: 12px 0;
    }

    /* Run and Pass play labels */
    .run-label {
        display: inline-block;
        background-color: #276749;
        color: #F5F0E1;
        padding: 6px 12px;
        border-radius: 6px;
        font-weight: bold;
        margin: 5px 0;
    }

    .pass-label {
        display: inline-block;
        background-color: #2B6CB0;
        color: #F5F0E1;
        padding: 6px 12px;
        border-radius: 6px;
        font-weight: bold;
        margin: 5px 0;
    }

    /* Favorite indicator */
    .favorite-label {
        display: inline-block;
        background-color: #8B6B24;
        color: #FFF4CC;
        padding: 6px 12px;
        border-radius: 6px;
        font-weight: bold;
        margin: 5px 0;
    }
""")


# ==================================================
# CONSTANTS
# ==================================================

PLAY_TYPES = ["Run", "Pass"]

FORMATIONS = [
    "Shotgun",
    "I-Formation",
    "Pistol",
    "Singleback",
    "Empty",
    "Wildcat",
    "Trips"
]


# ==================================================
# FORMATION INFORMATION
# ==================================================

FORMATION_INFO = {
    "Shotgun": {
        "personnel": (
            "Commonly 11 personnel: 1 running back, "
            "1 tight end, and 3 wide receivers."
        ),
        "positioning": (
            "The quarterback stands several yards behind the center. "
            "The running back lines up beside or behind the quarterback. "
            "Five offensive linemen line up across the line of scrimmage. "
            "Wide receivers spread toward the sidelines. "
            "The tight end lines up beside the offensive line "
            "or farther out as a receiver."
        )
    },

    "I-Formation": {
        "personnel": (
            "Commonly 21 personnel: 2 running backs, "
            "1 tight end, and 2 wide receivers."
        ),
        "positioning": (
            "The quarterback lines up directly behind the center. "
            "The fullback lines up behind the quarterback, "
            "and the running back lines up behind the fullback. "
            "Five offensive linemen line up across the line of scrimmage. "
            "Wide receivers line up toward the outside. "
            "The tight end usually lines up beside the offensive line."
        )
    },

    "Pistol": {
        "personnel": (
            "Commonly 11 personnel: 1 running back, "
            "1 tight end, and 3 wide receivers."
        ),
        "positioning": (
            "The quarterback stands a few yards behind the center. "
            "The running back lines up directly behind the quarterback. "
            "Five offensive linemen line up across the line of scrimmage. "
            "Wide receivers spread toward the sidelines. "
            "The tight end can line up beside the offensive line "
            "or split out."
        )
    },

    "Singleback": {
        "personnel": (
            "Commonly 11 personnel: 1 running back, "
            "1 tight end, and 3 wide receivers."
        ),
        "positioning": (
            "The quarterback lines up directly behind the center. "
            "One running back lines up behind the quarterback. "
            "Five offensive linemen line up across the line of scrimmage. "
            "Wide receivers spread out, and the tight end "
            "usually lines up beside the offensive line."
        )
    },

    "Empty": {
        "personnel": (
            "Commonly 10 or 11 personnel, with no running back "
            "positioned in the backfield. The offense uses "
            "wide receivers and tight ends spread across the field."
        ),
        "positioning": (
            "The quarterback lines up in shotgun formation. "
            "Five offensive linemen line up across the line of scrimmage. "
            "The remaining eligible receivers spread out across the field. "
            "A running back may line up as a wide receiver."
        )
    },

    "Wildcat": {
        "personnel": (
            "Personnel varies, but commonly includes multiple "
            "running backs, a tight end, and wide receivers."
        ),
        "positioning": (
            "A running back or another non-quarterback player "
            "lines up behind the center to receive the direct snap. "
            "Other running backs may line up beside or behind "
            "the player receiving the snap. Receivers spread out "
            "to create blocking and passing opportunities."
        )
    },

    "Trips": {
        "personnel": (
            "Commonly 11 personnel: 1 running back, "
            "1 tight end, and 3 wide receivers."
        ),
        "positioning": (
            "Three wide receivers line up together on one side "
            "of the field. The tight end usually lines up on "
            "the opposite side or beside the offensive line. "
            "The quarterback lines up behind the center, and "
            "the running back lines up in the backfield."
        )
    }
}


# ==================================================
# DATACLASSES
# ==================================================

@dataclass
class Play:
    """Store information about one football play.

    Attributes:
        name (str): The name of the football play.
        play_type (str): The type of play, Run or Pass.
        formation (str): The offensive formation used.
        description (str): A description of how the play works.
        favorite (bool): Whether the play is marked as a favorite.
    """
    name: str
    play_type: str
    formation: str
    description: str
    favorite: bool = False


@dataclass
class State:
    """Store information used throughout the website.

    Attributes:
        plays (list[Play]): All football plays saved in the playbook.
        selected_play_index (int): The index of the currently selected play.
        search_text (str): The user's current play name search.
        play_type_filter (str): The selected Run or Pass filter.
        selected_formation (str): The currently selected formation.
        status_message (str): A message displayed to the user.
    """
    plays: list[Play]
    selected_play_index: int
    search_text: str
    play_type_filter: str
    selected_formation: str
    status_message: str


# ==================================================
# HELPER FUNCTIONS
# ==================================================

def page_heading(title: str, subtitle: str) -> list:
    """Create a consistent heading section for a website page.

    Parameters:
        title (str): The main heading displayed on the page.
        subtitle (str): The smaller description below the heading.

    Returns:
        list: A list containing the formatted page heading.
    """
    return [
        Div(
            Header(title),
            Text(subtitle, classes="subtitle"),
            classes="page-banner"
        )
    ]


def navigation_buttons() -> Div:
    """Create the navigation buttons used throughout the website.

    Parameters:
        None

    Returns:
        Div: A navigation section containing buttons for Home,
        My Playbook, Favorites, Create Play, and Formations.
    """
    return Div(
        Button("Home", "index"),
        Button("My Playbook", "playbook"),
        Button("Favorites", "favorites"),
        Button("Create Play", "create_play"),
        Button("Formations", "formations"),
        classes="navigation"
    )


def play_type_label(play_type: str):
    """Display a colored label based on the type of football play.

    Parameters:
        play_type (str): The type of play, either Run or Pass.

    Returns:
        Text: A green label for a Run play or a blue label
        for a Pass play.
    """
    if play_type == "Run":
        return Text("RUN PLAY", classes="run-label")
    else:
        return Text("PASS PLAY", classes="pass-label")


def play_matches_filters(
    play: Play,
    search_text: str,
    play_type_filter: str
) -> bool:
    """Check whether a play matches the user's search and play type filters.

    Parameters:
        play (Play): The play being checked.
        search_text (str): The text entered by the user.
        play_type_filter (str): The selected play type filter.

    Returns:
        bool: True if the play matches both filters, or False otherwise.
    """
    name_matches = search_text.lower() in play.name.lower()

    type_matches = (
        play_type_filter == "All"
        or play.play_type == play_type_filter
    )

    return name_matches and type_matches


def valid_play_index(state: State, play_index: int) -> bool:
    """Check whether a play index is within the valid range of saved plays.

    Parameters:
        state (State): The current website state containing saved plays.
        play_index (int): The index of the play being checked.

    Returns:
        bool: True if the index identifies an existing play,
        or False if the index is invalid.
    """
    return 0 <= play_index < len(state.plays)


# ==================================================
# PAGE 1: HOME
# ==================================================

@route
def index(state: State) -> Page:
    """Display the homepage and the playbook dashboard.

    Parameters:
        state (State): The current website state containing saved plays,
        search settings, selected information, and status messages.

    Returns:
        Page: The homepage with playbook statistics, navigation buttons,
        status messages, and quick actions.
    """
    run_count = 0
    pass_count = 0

    for play in state.plays:
        if play.play_type == "Run":
            run_count += 1
        elif play.play_type == "Pass":
            pass_count += 1

    content = page_heading(
        "FOOTBALL PLAYBOOK",
        "Your personal space to organize and manage football plays."
    )

    content.append(navigation_buttons())

    content.append(
        Header("Playbook Dashboard", level=2)
    )

    content.append(
        Div(
            Header(str(len(state.plays)), level=1),
            Text("Total Saved Plays"),
            classes="info-card"
        )
    )

    content.append(
        Div(
            Text("RUN PLAYS", classes="field-label"),
            Header(str(run_count), level=2),
            classes="info-card"
        )
    )

    content.append(
        Div(
            Text("PASS PLAYS", classes="field-label"),
            Header(str(pass_count), level=2),
            classes="info-card"
        )
    )

    content.append(
        Div(
            Text(state.status_message),
            classes="notice"
        )
    )

    content.append(Header("Quick Actions", level=2))

    content.append(
        Div(
            Button("View My Playbook", "playbook"),
            Button("View Favorites", "favorites"),
            Button("Create a New Play", "create_play"),
            Button("Explore Formations", "formations"),
            classes="navigation"
        )
    )

    return Page(state, content)


# ==================================================
# PAGE 2: PLAYBOOK
# ==================================================

@route
def playbook(state: State) -> Page:
    """Display all saved plays that match the user's search and filters.

    Parameters:
        state (State): The current website state containing the plays
        and the user's selected search and filter settings.

    Returns:
        Page: The playbook page displaying matching plays, their
        formations, colored play type labels, and favorite indicators.
    """
    content = page_heading(
        "MY PLAYBOOK",
        "Browse, search, and organize your saved football plays."
    )

    content.append(navigation_buttons())

    content.append(
        Header("Search and Filter", level=2)
    )

    content.append(
        Text("Search by play name:", classes="field-label")
    )

    content.append(
        TextBox("search_text", state.search_text)
    )

    content.append(
        Text("Filter by play type:", classes="field-label")
    )

    content.append(
        SelectBox(
            "play_type_filter",
            ["All", "Run", "Pass"],
            state.play_type_filter
        )
    )

    content.append(Button("Apply Filters", "filter_plays"))

    content.append(
        Div(state.status_message, classes="notice")
    )

    content.append(
        Header("Saved Plays", level=2)
    )

    found_play = False

    for index_number, play in enumerate(state.plays):

        if play_matches_filters(
            play,
            state.search_text,
            state.play_type_filter
        ):
            found_play = True

            play_card = Div(
                Header(play.name, level=3),
                play_type_label(play.play_type),

                Text(
                    "★ FAVORITE",
                    classes="favorite-label"
                ) if play.favorite else Text(""),

                Text("FORMATION: " + play.formation),

                Button(
                    "View Play Details",
                    "play_details",
                    [Argument("play_index", index_number)]
                ),
                classes="play-card"
            )

            content.append(play_card)

    if not found_play:
        content.append(
            Div(
                "No matching plays were found. "
                "Try changing your search or filters.",
                classes="info-card"
            )
        )

    return Page(state, content)


# ==================================================
# FILTER PLAYS
# ==================================================

@route
def filter_plays(
    state: State,
    search_text: str,
    play_type_filter: str
) -> Page:
    """Save the user's search text and play type filter selections.

    Parameters:
        state (State): The current website state.
        search_text (str): The text entered into the search box.
        play_type_filter (str): The selected filter, such as All,
        Run, or Pass.

    Returns:
        Page: The updated playbook page displaying plays that
        match the selected filters.
    """
    state.search_text = search_text
    state.play_type_filter = play_type_filter
    state.status_message = "Your filters have been updated."

    return playbook(state)


# ==================================================
# PAGE 3: CREATE A PLAY
# ==================================================

@route
def create_play(state: State) -> Page:
    """Display a form that allows the user to create a new football play.

    Parameters:
        state (State): The current website state.

    Returns:
        Page: A page containing input fields for the play name,
        play type, formation, and description.
    """
    content = page_heading(
        "CREATE A PLAY",
        "Enter the information below to add a play to your playbook."
    )

    content.append(navigation_buttons())

    content.append(
        Header("Play Information", level=2)
    )

    content.append(
        Text("PLAY NAME", classes="field-label")
    )

    content.append(TextBox("name"))

    content.append(
        Text("PLAY TYPE", classes="field-label")
    )

    content.append(
        SelectBox("play_type", PLAY_TYPES, "Run")
    )

    content.append(
        Text("FORMATION", classes="field-label")
    )

    content.append(
        SelectBox("formation", FORMATIONS, "Shotgun")
    )

    content.append(
        Text("PLAY DESCRIPTION", classes="field-label")
    )

    content.append(
        TextArea("description", "", rows=5)
    )

    content.append(
        Text(
            "Tip: Include details about blocking, player movement, "
            "and the intended result."
        )
    )

    content.append(Button("Save My Play", "save_play"))

    content.append(
        Div(state.status_message, classes="notice")
    )

    return Page(state, content)


# ==================================================
# SAVE A NEW PLAY
# ==================================================

@route
def save_play(
    state: State,
    name: str,
    play_type: str,
    formation: str,
    description: str
) -> Page:
    """Validate the information entered by the user and save a new play.

    Parameters:
        state (State): The current website state containing saved plays.
        name (str): The name entered for the new play.
        play_type (str): The selected type of play, Run or Pass.
        formation (str): The selected offensive formation.
        description (str): The description of the new football play.

    Returns:
        Page: The updated playbook page if the play is saved,
        or the create play page if validation fails.
    """
    if name.strip() == "":
        state.status_message = "Error: Please enter a play name."
        return create_play(state)

    if play_type not in PLAY_TYPES:
        state.status_message = "Error: Choose a valid play type."
        return create_play(state)

    if formation not in FORMATIONS:
        state.status_message = "Error: Choose a valid formation."
        return create_play(state)

    for play in state.plays:
        if play.name.lower() == name.strip().lower():
            state.status_message = (
                "Error: A play with that name already exists."
            )
            return create_play(state)

    new_play = Play(
        name.strip(),
        play_type,
        formation,
        description.strip()
    )

    state.plays.append(new_play)
    state.selected_play_index = len(state.plays) - 1
    state.status_message = "Success! Your play has been saved."

    return playbook(state)


# ==================================================
# PAGE 4: PLAY DETAILS
# ==================================================

@route
def play_details(
    state: State,
    play_index: int
) -> Page:
    """Display detailed information about a selected football play.

    Parameters:
        state (State): The current website state.
        play_index (int): The index of the selected play in the plays list.

    Returns:
        Page: A page showing the play's name, type, formation,
        description, favorite status, and available actions.
        Returns the playbook page if the index is invalid.
    """
    if not valid_play_index(state, play_index):
        state.status_message = "That play could not be found."
        return playbook(state)

    state.selected_play_index = play_index
    play = state.plays[play_index]

    content = page_heading(
        play.name.upper(),
        "Review the details of this football play."
    )

    content.append(navigation_buttons())

    content.append(
        Div(
            Text("PLAY TYPE", classes="field-label"),
            play_type_label(play.play_type),
            Text("FORMATION", classes="field-label"),
            Header(play.formation, level=3),

            Text(
                "★ FAVORITE",
                classes="favorite-label"
            ) if play.favorite else Text(""),

            classes="info-card"
        )
    )

    content.append(
        Header("Play Description", level=2)
    )

    content.append(
        Div(
            play.description if play.description else
            "No description has been added.",
            classes="info-card"
        )
    )

    if play.favorite:
        content.append(
            Button(
                "★ Remove from Favorites",
                "toggle_favorite",
                [Argument("play_index", play_index)]
            )
        )
    else:
        content.append(
            Button(
                "☆ Add to Favorites",
                "toggle_favorite",
                [Argument("play_index", play_index)]
            )
        )

    content.append(
        Button(
            "Edit This Play",
            "edit_play",
            [Argument("play_index", play_index)]
        )
    )

    content.append(
        Button(
            "Remove This Play",
            "delete_play",
            [Argument("play_index", play_index)]
        )
    )

    content.append(Button("Back to Playbook", "playbook"))

    return Page(state, content)


# ==================================================
# TOGGLE FAVORITE STATUS
# ==================================================

@route
def toggle_favorite(
    state: State,
    play_index: int
) -> Page:
    """Add a play to favorites or remove it from favorites.

    Parameters:
        state (State): The current website state containing saved plays.
        play_index (int): The index of the play whose favorite status
        should be changed.

    Returns:
        Page: The play details page showing the updated favorite status,
        or the playbook page if the index is invalid.
    """
    if not valid_play_index(state, play_index):
        state.status_message = "That play could not be found."
        return playbook(state)

    play = state.plays[play_index]

    play.favorite = not play.favorite

    if play.favorite:
        state.status_message = (
            play.name + " was added to your favorites!"
        )
    else:
        state.status_message = (
            play.name + " was removed from your favorites."
        )

    return play_details(state, play_index)


# ==================================================
# DELETE A PLAY
# ==================================================

@route
def delete_play(
    state: State,
    play_index: int
) -> Page:
    """Remove a selected football play from the playbook.

    Parameters:
        state (State): The current website state containing saved plays.
        play_index (int): The index of the play that should be deleted.

    Returns:
        Page: The updated playbook page with a message confirming
        that the play was removed, or the playbook page with an error
        message if the index is invalid.
    """
    if not valid_play_index(state, play_index):
        state.status_message = "That play could not be found."
        return playbook(state)

    removed_play = state.plays.pop(play_index)

    state.selected_play_index = -1

    state.status_message = (
        removed_play.name + " was removed from your playbook."
    )

    return playbook(state)


# ==================================================
# PAGE 5: FAVORITES
# ==================================================

@route
def favorites(state: State) -> Page:
    """Display all football plays that the user has marked as favorites.

    Parameters:
        state (State): The current website state containing saved plays
        and their favorite statuses.

    Returns:
        Page: A page listing favorite plays with their names,
        formations, play type labels, and buttons to view details.
        Displays a message if there are no favorite plays.
    """
    content = page_heading(
        "MY FAVORITE PLAYS",
        "Your collection of favorite offensive plays."
    )

    content.append(navigation_buttons())

    content.append(
        Header("Favorite Plays", level=2)
    )

    found_favorite = False

    for index_number, play in enumerate(state.plays):

        if play.favorite:
            found_favorite = True

            content.append(
                Div(
                    Header(play.name, level=3),
                    Text("★ FAVORITE", classes="favorite-label"),
                    play_type_label(play.play_type),
                    Text("FORMATION: " + play.formation),
                    Button(
                        "View Play Details",
                        "play_details",
                        [Argument("play_index", index_number)]
                    ),
                    classes="play-card"
                )
            )

    if not found_favorite:
        content.append(
            Div(
                "You have not added any favorite plays yet. "
                "Visit your playbook and select a play to add it!",
                classes="info-card"
            )
        )

    content.append(Button("Back to My Playbook", "playbook"))

    return Page(state, content)


# ==================================================
# PAGE 6: EDIT A PLAY
# ==================================================

@route
def edit_play(state: State, play_index: int) -> Page:
    """Display a form for editing an existing football play.

    Parameters:
        state (State): The current website state.
        play_index (int): The index of the play that will be edited.

    Returns:
        Page: A page containing the selected play's current information
        in editable input fields, or the playbook page if the index
        is invalid.
    """
    if not valid_play_index(state, play_index):
        state.status_message = "That play could not be found."
        return playbook(state)

    state.selected_play_index = play_index
    play = state.plays[play_index]

    content = page_heading(
        "EDIT PLAY",
        "Update the information for your selected play."
    )

    content.append(navigation_buttons())

    content.append(
        Text("PLAY NAME", classes="field-label")
    )

    content.append(TextBox("name", play.name))

    content.append(
        Text("PLAY TYPE", classes="field-label")
    )

    content.append(
        SelectBox("play_type", PLAY_TYPES, play.play_type)
    )

    content.append(
        Text("FORMATION", classes="field-label")
    )

    content.append(
        SelectBox("formation", FORMATIONS, play.formation)
    )

    content.append(
        Text("PLAY DESCRIPTION", classes="field-label")
    )

    content.append(
        TextArea("description", play.description, rows=5)
    )

    content.append(
        Button(
            "Save Changes",
            "save_edit",
            [Argument("play_index", play_index)]
        )
    )

    content.append(
        Button(
            "Cancel",
            "play_details",
            [Argument("play_index", play_index)]
        )
    )

    return Page(state, content)


# ==================================================
# SAVE EDITED PLAY
# ==================================================

@route
def save_edit(
    state: State,
    play_index: int,
    name: str,
    play_type: str,
    formation: str,
    description: str
) -> Page:
    """Validate and save changes to an existing football play.

    Parameters:
        state (State): The current website state containing saved plays.
        play_index (int): The index of the play being edited.
        name (str): The updated name of the play.
        play_type (str): The updated play type, Run or Pass.
        formation (str): The updated offensive formation.
        description (str): The updated play description.

    Returns:
        Page: The updated play details page if the changes are saved,
        or the edit page if validation fails.
    """
    if not valid_play_index(state, play_index):
        state.status_message = "That play could not be found."
        return playbook(state)

    if name.strip() == "":
        state.status_message = "Error: The play name cannot be empty."
        return edit_play(state, play_index)

    if play_type not in PLAY_TYPES or formation not in FORMATIONS:
        state.status_message = "Error: Please select valid options."
        return edit_play(state, play_index)

    for index_number, other_play in enumerate(state.plays):
        if (
            index_number != play_index
            and other_play.name.lower() == name.strip().lower()
        ):
            state.status_message = (
                "Error: Another play already uses that name."
            )
            return edit_play(state, play_index)

    play = state.plays[play_index]

    play.name = name.strip()
    play.play_type = play_type
    play.formation = formation
    play.description = description.strip()

    state.status_message = "Success! Your changes have been saved."

    return play_details(state, play_index)


# ==================================================
# PAGE 7: FORMATIONS
# ==================================================

@route
def formations(state: State) -> Page:
    """Display the available offensive formations and their descriptions.

    Parameters:
        state (State): The current website state.

    Returns:
        Page: A formations page displaying each formation's typical
        personnel, player positioning, and a button to explore details.
    """
    content = page_heading(
        "OFFENSIVE FORMATIONS",
        "Learn how offensive players line up before the snap."
    )

    content.append(navigation_buttons())

    content.append(
        Header("Available Formations", level=2)
    )

    for formation_name in FORMATIONS:

        info = FORMATION_INFO[formation_name]

        formation_card = Div(
            Header(formation_name, level=2),

            Text("TYPICAL PERSONNEL", classes="field-label"),
            info["personnel"],

            Text("PLAYER POSITIONING", classes="field-label"),
            info["positioning"],

            Button(
                "Explore This Formation",
                "formation_details",
                [Argument("formation_name", formation_name)]
            ),

            classes="info-card"
        )

        content.append(formation_card)

    return Page(state, content)


# ==================================================
# PAGE 8: FORMATION DETAILS
# ==================================================

@route
def formation_details(
    state: State,
    formation_name: str
) -> Page:
    """Display detailed information about a selected offensive formation.

    Parameters:
        state (State): The current website state.
        formation_name (str): The name of the formation being displayed.

    Returns:
        Page: A page showing the formation's typical personnel,
        player positioning, and saved plays that use the formation.
        Returns the formations page if the formation is invalid.
    """
    if formation_name not in FORMATION_INFO:
        state.status_message = "Formation not found."
        return formations(state)

    state.selected_formation = formation_name
    info = FORMATION_INFO[formation_name]

    content = page_heading(
        formation_name.upper(),
        "Learn about the personnel and player alignment."
    )

    content.append(navigation_buttons())

    content.append(
        Header("Typical Personnel", level=2)
    )

    content.append(
        Div(info["personnel"], classes="info-card")
    )

    content.append(
        Header("Player Positioning", level=2)
    )

    content.append(
        Div(info["positioning"], classes="info-card")
    )

    content.append(
        Header("Plays Using This Formation", level=2)
    )

    found_play = False

    for index_number, play in enumerate(state.plays):

        if play.formation == formation_name:
            found_play = True

            content.append(
                Div(
                    Header(play.name, level=3),
                    play_type_label(play.play_type),
                    Button(
                        "View Play",
                        "play_details",
                        [Argument("play_index", index_number)]
                    ),
                    classes="play-card"
                )
            )

    if not found_play:
        content.append(
            Div(
                "There are no saved plays using this formation yet.",
                classes="info-card"
            )
        )

    content.append(Button("Back to Formations", "formations"))

    return Page(state, content)


# ==================================================
# SITE INFORMATION
# ==================================================

set_site_information(
    author="Your Name",
    description=(
        "A football playbook organizer for creating, "
        "searching, editing, favoriting, and learning offensive plays."
    ),
    sources=[
        "Original project created using Python and Drafter."
    ],
    planning="Football Playbook Organizer final project plan.",
    links=[]
)


# ==================================================
# START WEBSITE
# ==================================================

start_server(
    State(
        plays=[
            Play(
                "Inside Zone",
                "Run",
                "Shotgun",
                "The offensive line blocks inside while "
                "the running back follows the blocking.",
                True
            ),

            Play(
                "Four Verticals",
                "Pass",
                "Shotgun",
                "The receivers run deep vertical routes "
                "to stretch the defense."
            ),

            Play(
                "Power",
                "Run",
                "I-Formation",
                "The offense uses pulling blockers to "
                "create space for the running back.",
                True
            )
        ],

        selected_play_index=-1,
        search_text="",
        play_type_filter="All",
        selected_formation="",
        status_message="Welcome to your football playbook!"
    )
)

