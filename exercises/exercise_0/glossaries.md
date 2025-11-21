| **Terminology** | **Explanation** |
| --- | --- |
| **few-shot learning** | A prompting technique where you provide a model with a few examples of tasks so it can infer the pattern and produce similar outputs. |
| **token** | A unit of text the model reads — can be a character, word piece, or symbol. Models process and count text in tokens, not characters. |
| **context window** | The maximum number of tokens a model can consider at once, including both input and output. |
| **pydantic** | A Python library for data validation and settings management using Python type hints. It creates structured, validated models. |
| **BaseModel** | The core Pydantic class used to define data models with type validation, default values, and helper methods. |
| **Field** | A Pydantic helper used to add metadata, default values, constraints, or descriptions to a model’s fields. |
| **model_fields** | A Pydantic attribute that stores metadata about a model’s defined fields (names, types, defaults, etc.). |
| **computed_field** | A Pydantic decorator that declares a property as a field computed from other data, included during model output. |
| **model_validate** | A Pydantic method used to validate and create a model instance from raw input (dicts, objects, JSON, etc.). |
| **model_dump** | A Pydantic method that outputs a model’s data as a dictionary, optionally controlling serialization settings. |
| **type hinting** | Annotating variables, function parameters, and return types to improve clarity, tooling, and static analysis. |
| **serialization** | Converting a Python object or model into a format like JSON or a dictionary for storage or transmission. |
| **deserialization** | Converting serialized data (like JSON) back into Python objects or models. |
| **prompt engineering** | The craft of designing instructions, examples, and structures to guide an AI model toward desired outputs. |
| **zero-shot learning** | A prompting technique where the model performs a task without being shown any examples—only instructions. |