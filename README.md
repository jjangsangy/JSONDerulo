# JSONDerulo
A JSON based serialization that is dirty to talk about

## Usage

```JSON

$ derulo [--version, -v]
  "JSONDerulo version JSONDerulo" 
  
```

# Basic Usage
```sh
$ derulo --say --output=json
```
```JSON
{
  "JSONDerulo": "whatcha say"
}
```

## Syntactic Sugar
```sh
$ derulo --say --output=json
```
```JSON
{
  "JSONDerulo": "whatcha say"
}
```

# Keyword Based Usage

```sh
$ derulo relationships
```
```JSON
{
  "JSONDerulo": "Marry Me"
}
```

# 
```
{
  "JSONDerulo":
      "IS THERE SUCH A THING AS A CONNECTED CASTLE?",
}

```

## Stream Output
```sh
$ derulo --stream solo
```
```JSON
  "JSONDerulo": 
      [
        "Riding solo, soooooloooo",
        "yeah it's like",
            "S", "O", "L", "O",
            "S", "O", "L", "O",
            "S", "O", "L", "O",
            "S", "O", "L", "O"
      ]
}

```


## Known Issues

Infinite recursive calls

```
$ derulo --say derulo
```
```JSON
{
  "JSONDerulo": {
    "JSONDerulo": {
      "JSONDerulo": {
        "JSONDerulo": {
          "JSONDerulo": {
            "JSONDerulo": ...
          }
        }
      }
    }
  }
}}
```

Undefined Behavior

```
$ derulo --say

```
