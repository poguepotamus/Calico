[Workspace]: (./Workspace.md)

# Users

A logical description of Calico users.

## Data

A user is the representation of an end user. This contains information about the workspaces the user has joined, as well as login information.

### Logical Structure

<table style="text-align: center;">
	<tr>
		<td> User ID </td>
		<td> Username </td>
	</tr> <tr>
		<td> SaltHash </td>
		<td> Password </td>
	</tr> <tr>
		<td> Email </td>
		<td> Workspaces </td>
	</tr>
</table>

### Logical Definitions

 Name       | Logical encoding      | Data type
------------|-----------------------|-----------
User ID     | None                  | `int`
Username    | None                  | `str`
Salt hash   | None                  | `str`
Password    | SHA256(salt+pw)       | `int`
Email       | None                  | `str`
Workspaces  | None                  | `int`

### Table Structure

User ID | Username | SaltHash | Password | Email | Workspaces
-|-|-|-|-|-
`00000001` | poguepotamus | E1F53135E559C253 | 439CC56E718301D55AFBE1164E3167FFD87B0DFB17B80BEA0B3E43DD8D20A580 | matthewpogue606@gmail.com | [`00000001`]

