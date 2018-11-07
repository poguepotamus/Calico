[Workspace]: (./Workspace.md)

# Users

A logical description of Calico users.

## Data

A user is the representation of an end user. This contains information about the workspaces the user has joined, as well as login information.

> This structure uses another structure, [Workspace](Workspace)

### Logical Structure

User ID | Username | Password | Email | Workspaces
-|-|-|-|-|-
`00000001` | poguepotamus | hahauwish | matthewpogue606@gmail.com | [`00000001`]

### Logical definitions

 Name       | Logical encoding      | Data type
------------|-----------------------|-----------
User ID     | None                  | `int`
Username    | None                  | `str`
Password    | Base64                | `int`
Email       | None                  | `str`
Workspaces  | None                  | `int`