type = input("File name: ").strip().lower().split('.')
if len(type) == 1:
    print("application/octet-stream")
else:
    type = type[len(type)-1]
    match type:
        case "gif":
            print("image/gif")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")