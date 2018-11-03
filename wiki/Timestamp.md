# Logical description of timestamps

This page describes the timestamp class used in other calico structures.

## Logical Data

The timestamp is constructed to allow an accurate representation of time in a small form.

### Logical structure

<table>
	<tr>
		<td> Start time </td>
		<td> Duration </td>
		<td> Time zone </td>
	</tr>
</table>

### Logical definitions

  Name      | Logical encoding      | Data type
------------|-----------------------|-----------
Start time  | Unix timestamp in UCT | `int`
Duration    | In seconds (Unix)     | `int`
Time zone   | UTC Offset in hours   | `int`

### Example

<table>
	<tr>
		<td> 1520035200 </td>
		<td> 86400 </td>
		<td> 5 </td>
	</tr>
</table>

This is a Unix timestamp of my birthday (The full day), March 3rd, 2018.  
The duration is set to be all day (24 hours x 60 minutes x 60 seconds).  
I live currently in Wichita Kansas, which has a UTC offset of `5`. In practice, I wouldn't want to use a timestamp, thus it will trigger at midnight at my local time, wherever I may be.
