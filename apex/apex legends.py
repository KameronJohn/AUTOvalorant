from apex_main import apex
def legends_preference():
    """ config """
    a.all_agents = {
        "assault": ["bangalore", "fuse", "ash", "maggie","ballistic"],
        "skirmisher": ["horizon", "pathfinder","wraith","valkyrie","octane","revenant"],
        "recon": ["bloodhound", "seer","vantage","crypto"],
        "support": ["gibraltar", "lifeline","loba","newcastle","conduit"],
        "controller": ["rampart", "caustic", "catalyst","wattson"]
    }
    """ config """
    """ preferences """
    a.preferences = dict()
    a.force_pick = False
    a.preferences["skirmisher"] = "pathfinder"
    a.preferences["recon"] = "vantage"
    a.preferences["controller"] = "rampart"
    a.preferences["support"] = "loba"
    a.preferences["assault"] = "bangalore"
    """  """
    # a.preferences = ["pathfinder","vantage","bangalore"]
    # a.preferences = ["rampart","fuse","seer"]
    # a.preferences = ["ash","pathfinder","vantage"]
    """ preferences """
if __name__ == '__main__' :
    a = apex()
    legends_preference()
    a.checkScenerio()
    # chop_image.main()