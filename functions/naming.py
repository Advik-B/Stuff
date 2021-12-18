def name(link:str):
    """Will name a file based on the link given"""
    # If the link is empty, raise an error
    if link == "":
        raise ValueError("Link is empty")
    else:
        return link.split('/')[-1]