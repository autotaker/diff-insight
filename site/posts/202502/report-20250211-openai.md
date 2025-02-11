---
date: '2025-02-11'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:879fbd3...MicrosoftDocs:f57bd77
summary: このコードの差分は、Azure OpenAIを利用する開発者向けドキュメントに対する複数の更新と改良を導入しています。主な変更点は、Python、.NET、REST
  API向けの構造化出力に関する新しいガイドが追加されたことです。このガイドには具体的な使用例と詳細な実装方法が含まれており、開発者が迅速に機能を統合できるよう設計されています。また、ドキュメント内のサービス名の変更や日付情報の更新、目次の微調整も行われています。この更新によって、開発者はAzure
  OpenAIの技術をより効果的に活用することが可能になります。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:879fbd3...MicrosoftDocs:f57bd77){target="_blank"}

# ハイライト

このコードの差分は、Azure OpenAIを活用する開発者向けのドキュメントに対して複数の更新と改良を導入しています。最も注目すべきは、構造化出力に関する新しいガイドの追加です。Python、.NET、REST APIの各プラットフォーム向けに、具体的な使用例とともに詳細な実装方法を提供しています。また、サービス名変更や日付情報の更新、目次の微調整が行われています。

## 新機能

- Python、.NET、REST API用の構造化出力ガイドが新たに追加され、各プラットフォームでの具体的な実装例と設定手順が提供されました。
- .NET、Python、REST APIそれぞれに特化したコード例や実装ガイドが含まれ、開発者が迅速に機能を統合するのに役立ちます。

## 破壊的変更

特定の破壊的変更は報告されていませんが、アプリケーションやサービス名の変更により既存のシステム設定や呼び出しが影響を受ける可能性があります。

## その他の更新

- ドキュメントにはサービス名の変更が反映され、Azure AI StudioからAzure AI Foundryに名称が変更されています。
- .NET Coreアプリケーション名が「azure-openai-quickstart」から「azure-openai-assistants-quickstart」に変更され、対応する実行コマンドも更新されました。
- OpenAIのドキュメント目次に「データ、プライバシー、セキュリティ」という新しいセクションが追加されました。

# インサイト

この更新は、Azure OpenAIサービスの構造化出力を利用するための開発者向けドキュメントが大幅に強化されていることを示しています。これにより、異なるプラットフォーム (.NET, Python, REST API) における開発が容易になり、より正確かつ効率的な実装が可能になります。

新たに提供されたガイドは、特にビジネスアプリケーションにおいて構造化データが求められる場面での使用を想定しています。これは、Azure OpenAIの能力を最大限活用した高度な開発をサポートするもので、実際の業務状況に即した具体的な実装方法が紹介されています。このことで、開発者は自分たちのプロジェクトにAzure AIの最新技術を迅速に組み込むことができるようになります。

また、サービス名やアプリケーション名の変更は、小さな更新に見えますが、今後の開発フローやドキュメンテーションの整合性を保つために重要です。これらの更新を適切に反映することで、ユーザーが現在のサービス状況を正しく把握し、対応する技術リソースを利用しやすくなることが期待されます。

さらに、目次の更新は利用者が必要な情報に素早くアクセスできるようにするための重要な調整です。特に、新たに追加された「データ、プライバシー、セキュリティ」セクションによって、データ保護に関する法律的側面へのアクセスが改善されています。これは、ユーザーがプライバシーやセキュリティに関連する最新の規制を理解し、適応する助けになります。

総じて、このドキュメントの更新は、開発者がAzure OpenAIの能力を最大限に引き出すための強力なリソースを提供するものであり、迅速で確実なプロジェクト遂行を支援するための価値ある一歩と言えます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [structured-outputs.md](#item-cc2557) | minor update | 構造化出力に関するドキュメントの更新 | modified | 134 | 533 | 667 | 
| [assistants-ai-studio.md](#item-1632e2) | minor update | Azure AI Studioのサービス名の変更 | modified | 1 | 1 | 2 | 
| [assistants-csharp.md](#item-cc4697) | minor update | .NET Coreアプリケーション名の変更 | modified | 2 | 2 | 4 | 
| [fine-tuning-openai-in-ai-studio.md](#item-723c8d) | minor update | Azure AI Studioのサービス名の変更 | modified | 1 | 1 | 2 | 
| [standard-global.md](#item-17a84b) | minor update | モデルマトリックスの更新 | modified | 26 | 26 | 52 | 
| [structured-outputs-dotnet.md](#item-4dd0a4) | new feature | 構造化出力のための.NETガイドの追加 | added | 321 | 0 | 321 | 
| [structured-outputs-python.md](#item-2734f0) | new feature | 構造化出力のためのPythonガイドの追加 | added | 255 | 0 | 255 | 
| [structured-outputs-rest.md](#item-c2c1a0) | new feature | REST APIによる構造化出力ガイドの追加 | added | 180 | 0 | 180 | 
| [toc.yml](#item-c945af) | minor update | 目次の更新にデータとプライバシーセクションの追加 | modified | 2 | 0 | 2 | 


# Modified Contents
## articles/ai-services/openai/how-to/structured-outputs.md{#item-cc2557}

<details>
<summary>Diff</summary>
````diff
@@ -10,6 +10,7 @@ ms.date: 01/30/2025
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
+zone_pivot_groups: structured-outputs
 ---
 
 # Structured outputs
@@ -33,426 +34,26 @@ Structured outputs make a model follow a [JSON Schema](https://json-schema.org/o
 
 Support for structured outputs was first added in API version `2024-08-01-preview`. It is available in the latest preview APIs as well as the latest GA API: `2024-10-21`.
 
-## Getting started
 
-# [Python (Microsoft Entra ID)](#tab/python-secure)
+::: zone pivot="programming-language-python"
 
-You can use [`Pydantic`](https://docs.pydantic.dev/latest/) to define object schemas in Python. Depending on what version of the [OpenAI](https://pypi.org/project/openai/) and [`Pydantic` libraries](https://pypi.org/project/pydantic/) you're running you might need to upgrade to a newer version. These examples were tested against `openai 1.42.0` and `pydantic 2.8.2`.
+[!INCLUDE [structured-outputs-python](../includes/structured-outputs-python.md)]
 
-```cmd
-pip install openai pydantic --upgrade
-```
-
-If you are new to using Microsoft Entra ID for authentication see [How to configure Azure OpenAI Service with Microsoft Entra ID authentication](./managed-identity.md).
-
-```python
-from pydantic import BaseModel
-from openai import AzureOpenAI
-from azure.identity import DefaultAzureCredential, get_bearer_token_provider
-
-token_provider = get_bearer_token_provider(
-    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
-)
-
-client = AzureOpenAI(
-  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
-  azure_ad_token_provider=token_provider,
-  api_version="2024-10-21"
-)
-
-
-class CalendarEvent(BaseModel):
-    name: str
-    date: str
-    participants: list[str]
-
-completion = client.beta.chat.completions.parse(
-    model="MODEL_DEPLOYMENT_NAME", # replace with the model deployment name of your gpt-4o 2024-08-06 deployment
-    messages=[
-        {"role": "system", "content": "Extract the event information."},
-        {"role": "user", "content": "Alice and Bob are going to a science fair on Friday."},
-    ],
-    response_format=CalendarEvent,
-)
-
-event = completion.choices[0].message.parsed
-
-print(event)
-print(completion.model_dump_json(indent=2))
-```
-
-### Output
-
-```json
-name='Science Fair' date='Friday' participants=['Alice', 'Bob']
-{
-  "id": "chatcmpl-A1EUP2fAmL4SeB1lVMinwM7I2vcqG",
-  "choices": [
-    {
-      "finish_reason": "stop",
-      "index": 0,
-      "logprobs": null,
-      "message": {
-        "content": "{\n  \"name\": \"Science Fair\",\n  \"date\": \"Friday\",\n  \"participants\": [\"Alice\", \"Bob\"]\n}",
-        "refusal": null,
-        "role": "assistant",
-        "function_call": null,
-        "tool_calls": [],
-        "parsed": {
-          "name": "Science Fair",
-          "date": "Friday",
-          "participants": [
-            "Alice",
-            "Bob"
-          ]
-        }
-      }
-    }
-  ],
-  "created": 1724857389,
-  "model": "gpt-4o-2024-08-06",
-  "object": "chat.completion",
-  "service_tier": null,
-  "system_fingerprint": "fp_1c2eaec9fe",
-  "usage": {
-    "completion_tokens": 27,
-    "prompt_tokens": 32,
-    "total_tokens": 59
-  }
-}
-```
-
-# [Python (key-based auth)](#tab/python)
-
-You can use [`Pydantic`](https://docs.pydantic.dev/latest/) to define object schemas in Python. Depending on what version of the [OpenAI](https://pypi.org/project/openai/) and [`Pydantic` libraries](https://pypi.org/project/pydantic/) you're running you might need to upgrade to a newer version. These examples were tested against `openai 1.42.0` and `pydantic 2.8.2`.
-
-```cmd
-pip install openai pydantic --upgrade
-```
-
-```python
-from pydantic import BaseModel
-from openai import AzureOpenAI
-
-client = AzureOpenAI(
-  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
-  api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
-  api_version="2024-10-21"
-)
-
-
-class CalendarEvent(BaseModel):
-    name: str
-    date: str
-    participants: list[str]
-
-completion = client.beta.chat.completions.parse(
-    model="MODEL_DEPLOYMENT_NAME", # replace with the model deployment name of your gpt-4o 2024-08-06 deployment
-    messages=[
-        {"role": "system", "content": "Extract the event information."},
-        {"role": "user", "content": "Alice and Bob are going to a science fair on Friday."},
-    ],
-    response_format=CalendarEvent,
-)
-
-event = completion.choices[0].message.parsed
-
-print(event)
-print(completion.model_dump_json(indent=2))
-```
-
-### Output
-
-```json
-name='Science Fair' date='Friday' participants=['Alice', 'Bob']
-{
-  "id": "chatcmpl-A1EUP2fAmL4SeB1lVMinwM7I2vcqG",
-  "choices": [
-    {
-      "finish_reason": "stop",
-      "index": 0,
-      "logprobs": null,
-      "message": {
-        "content": "{\n  \"name\": \"Science Fair\",\n  \"date\": \"Friday\",\n  \"participants\": [\"Alice\", \"Bob\"]\n}",
-        "refusal": null,
-        "role": "assistant",
-        "function_call": null,
-        "tool_calls": [],
-        "parsed": {
-          "name": "Science Fair",
-          "date": "Friday",
-          "participants": [
-            "Alice",
-            "Bob"
-          ]
-        }
-      }
-    }
-  ],
-  "created": 1724857389,
-  "model": "gpt-4o-2024-08-06",
-  "object": "chat.completion",
-  "service_tier": null,
-  "system_fingerprint": "fp_1c2eaec9fe",
-  "usage": {
-    "completion_tokens": 27,
-    "prompt_tokens": 32,
-    "total_tokens": 59
-  }
-}
-```
+::: zone-end
 
-# [REST](#tab/rest)
 
-`response_format` is set to `json_schema` with `strict: true` set.
+::: zone pivot="programming-language-csharp"
 
-```bash
-curl -X POST  https://YOUR_RESOURCE_NAME.openai.azure.com/openai/deployments/YOUR_MODEL_DEPLOYMENT_NAME/chat/completions?api-version=2024-10-21 \
-  -H "api-key: $AZURE_OPENAI_API_KEY" \
-  -H "Content-Type: application/json" \
-    -d '{
-        "messages": [
-                {"role": "system", "content": "Extract the event information."},
-                {"role": "user", "content": "Alice and Bob are going to a science fair on Friday."}
-            ],
-            "response_format": {
-                "type": "json_schema",
-                "json_schema": {
-                    "name": "CalendarEventResponse",
-                    "strict": true,
-                    "schema": {
-                        "type": "object",
-                        "properties": {
-                            "name": {
-                              "type": "string"
-                            },
-                            "date": {
-                                "type": "string"
-                            },
-                            "participants": {
-                                "type": "array",
-                                "items": {
-                                    "type": "string"
-                                }
-                            }
-                        },
-                        "required": [
-                            "name",
-                            "date",
-                            "participants"
-                        ],
-                        "additionalProperties": false
-                    }
-                }
-          }
-  }'
-```
+[!INCLUDE [structured-outputs-dotnet](../includes/structured-outputs-dotnet.md)]
 
-Output:
+::: zone-end
 
-```json
-{
-  "id": "chatcmpl-A1HKsHAe2hH9MEooYslRn9UmEwsag",
-  "object": "chat.completion",
-  "created": 1724868330,
-  "model": "gpt-4o-2024-08-06",
-  "choices": [
-    {
-      "index": 0,
-      "message": {
-        "role": "assistant",
-        "content": "{\n  \"name\": \"Science Fair\",\n  \"date\": \"Friday\",\n  \"participants\": [\"Alice\", \"Bob\"]\n}"
-      },
-      "logprobs": null,
-      "finish_reason": "stop"
-    }
-  ],
-  "usage": {
-    "prompt_tokens": 33,
-    "completion_tokens": 27,
-    "total_tokens": 60
-  },
-  "system_fingerprint": "fp_1c2eaec9fe"
-}
 
-```
+::: zone pivot="programming-language-rest"
 
----
-
-## Function calling with structured outputs
-
-Structured Outputs for function calling can be enabled with a single parameter, by supplying `strict: true`. 
-
-> [!NOTE]
-> Structured outputs are not supported with parallel function calls. When using structured outputs set `parallel_tool_calls` to `false`.
+[!INCLUDE [structured-outputs-rest](../includes/structured-outputs-rest.md)]
 
-# [Python (Microsoft Entra ID)](#tab/python-secure)
-
-```python
-from enum import Enum
-from typing import Union
-from pydantic import BaseModel
-import openai
-from openai import AzureOpenAI
-
-client = AzureOpenAI(
-  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
-  api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
-  api_version="2024-10-21"
-)
-
-
-class GetDeliveryDate(BaseModel):
-    order_id: str
-
-tools = [openai.pydantic_function_tool(GetDeliveryDate)]
-
-messages = []
-messages.append({"role": "system", "content": "You are a helpful customer support assistant. Use the supplied tools to assist the user."})
-messages.append({"role": "user", "content": "Hi, can you tell me the delivery date for my order #12345?"}) 
-
-response = client.chat.completions.create(
-    model="MODEL_DEPLOYMENT_NAME", # replace with the model deployment name of your gpt-4o 2024-08-06 deployment
-    messages=messages,
-    tools=tools
-)
-
-print(response.choices[0].message.tool_calls[0].function)
-print(response.model_dump_json(indent=2))
-```
-
-# [Python (key-based auth)](#tab/python)
-
-```python
-from enum import Enum
-from typing import Union
-from pydantic import BaseModel
-import openai
-from openai import AzureOpenAI
-
-client = AzureOpenAI(
-  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
-  api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
-  api_version="2024-10-21"
-)
-
-class GetDeliveryDate(BaseModel):
-    order_id: str
-
-tools = [openai.pydantic_function_tool(GetDeliveryDate)]
-
-messages = []
-messages.append({"role": "system", "content": "You are a helpful customer support assistant. Use the supplied tools to assist the user."})
-messages.append({"role": "user", "content": "Hi, can you tell me the delivery date for my order #12345?"}) 
-
-response = client.chat.completions.create(
-    model="MODEL_DEPLOYMENT_NAME", # replace with the model deployment name of your gpt-4o 2024-08-06 deployment
-    messages=messages,
-    tools=tools
-)
-
-print(response.choices[0].message.tool_calls[0].function)
-print(response.model_dump_json(indent=2))
-```
-
-# [REST](#tab/rest)
-
-```bash
-curl -X POST  https://YOUR_RESOURCE_NAME.openai.azure.com/openai/deployments/YOUR_MODEL_DEPLOYMENT_NAME/chat/completions?api-version=2024-10-21 \
-  -H "api-key: $AZURE_OPENAI_API_KEY" \
-  -H "Content-Type: application/json" \
-  -d '{
-  "messages": [
-    {
-      "role": "system",
-      "content": "You are a helpful assistant. The current date is August 6, 2024. You help users query for the data they are looking for by calling the query function."
-    },
-    {
-      "role": "user",
-      "content": "look up all my orders in may of last year that were fulfilled but not delivered on time"
-    }
-  ],
-  "tools": [
-    {
-      "type": "function",
-      "function": {
-        "name": "query",
-        "description": "Execute a query.",
-        "strict": true,
-        "parameters": {
-          "type": "object",
-          "properties": {
-            "table_name": {
-              "type": "string",
-              "enum": ["orders"]
-            },
-            "columns": {
-              "type": "array",
-              "items": {
-                "type": "string",
-                "enum": [
-                  "id",
-                  "status",
-                  "expected_delivery_date",
-                  "delivered_at",
-                  "shipped_at",
-                  "ordered_at",
-                  "canceled_at"
-                ]
-              }
-            },
-            "conditions": {
-              "type": "array",
-              "items": {
-                "type": "object",
-                "properties": {
-                  "column": {
-                    "type": "string"
-                  },
-                  "operator": {
-                    "type": "string",
-                    "enum": ["=", ">", "<", ">=", "<=", "!="]
-                  },
-                  "value": {
-                    "anyOf": [
-                      {
-                        "type": "string"
-                      },
-                      {
-                        "type": "number"
-                      },
-                      {
-                        "type": "object",
-                        "properties": {
-                          "column_name": {
-                            "type": "string"
-                          }
-                        },
-                        "required": ["column_name"],
-                        "additionalProperties": false
-                      }
-                    ]
-                  }
-                },
-                "required": ["column", "operator", "value"],
-                "additionalProperties": false
-              }
-            },
-            "order_by": {
-              "type": "string",
-              "enum": ["asc", "desc"]
-            }
-          },
-          "required": ["table_name", "columns", "conditions", "order_by"],
-          "additionalProperties": false
-        }
-      }
-    }
-  ]
-}'
-```
-
----
+::: zone-end
 
 ## Supported schemas and limitations
 
@@ -554,60 +155,60 @@ Example supported `anyOf` schema:
 
 ```json
 {
-	"type": "object",
-	"properties": {
-		"item": {
-			"anyOf": [
-				{
-					"type": "object",
-					"description": "The user object to insert into the database",
-					"properties": {
-						"name": {
-							"type": "string",
-							"description": "The name of the user"
-						},
-						"age": {
-							"type": "number",
-							"description": "The age of the user"
-						}
-					},
-					"additionalProperties": false,
-					"required": [
-						"name",
-						"age"
-					]
-				},
-				{
-					"type": "object",
-					"description": "The address object to insert into the database",
-					"properties": {
-						"number": {
-							"type": "string",
-							"description": "The number of the address. Eg. for 123 main st, this would be 123"
-						},
-						"street": {
-							"type": "string",
-							"description": "The street name. Eg. for 123 main st, this would be main st"
-						},
-						"city": {
-							"type": "string",
-							"description": "The city of the address"
-						}
-					},
-					"additionalProperties": false,
-					"required": [
-						"number",
-						"street",
-						"city"
-					]
-				}
-			]
-		}
-	},
-	"additionalProperties": false,
-	"required": [
-		"item"
-	]
+    "type": "object",
+    "properties": {
+        "item": {
+            "anyOf": [
+                {
+                    "type": "object",
+                    "description": "The user object to insert into the database",
+                    "properties": {
+                        "name": {
+                            "type": "string",
+                            "description": "The name of the user"
+                        },
+                        "age": {
+                            "type": "number",
+                            "description": "The age of the user"
+                        }
+                    },
+                    "additionalProperties": false,
+                    "required": [
+                        "name",
+                        "age"
+                    ]
+                },
+                {
+                    "type": "object",
+                    "description": "The address object to insert into the database",
+                    "properties": {
+                        "number": {
+                            "type": "string",
+                            "description": "The number of the address. Eg. for 123 main st, this would be 123"
+                        },
+                        "street": {
+                            "type": "string",
+                            "description": "The street name. Eg. for 123 main st, this would be main st"
+                        },
+                        "city": {
+                            "type": "string",
+                            "description": "The city of the address"
+                        }
+                    },
+                    "additionalProperties": false,
+                    "required": [
+                        "number",
+                        "street",
+                        "city"
+                    ]
+                }
+            ]
+        }
+    },
+    "additionalProperties": false,
+    "required": [
+        "item"
+    ]
 }
 ```
 
@@ -617,41 +218,41 @@ Supported example:
 
 ```json
 {
-	"type": "object",
-	"properties": {
-		"steps": {
-			"type": "array",
-			"items": {
-				"$ref": "#/$defs/step"
-			}
-		},
-		"final_answer": {
-			"type": "string"
-		}
-	},
-	"$defs": {
-		"step": {
-			"type": "object",
-			"properties": {
-				"explanation": {
-					"type": "string"
-				},
-				"output": {
-					"type": "string"
-				}
-			},
-			"required": [
-				"explanation",
-				"output"
-			],
-			"additionalProperties": false
-		}
-	},
-	"required": [
-		"steps",
-		"final_answer"
-	],
-	"additionalProperties": false
+    "type": "object",
+    "properties": {
+        "steps": {
+            "type": "array",
+            "items": {
+                "$ref": "#/$defs/step"
+            }
+        },
+        "final_answer": {
+            "type": "string"
+        }
+    },
+    "$defs": {
+        "step": {
+            "type": "object",
+            "properties": {
+                "explanation": {
+                    "type": "string"
+                },
+                "output": {
+                    "type": "string"
+                }
+            },
+            "required": [
+                "explanation",
+                "output"
+            ],
+            "additionalProperties": false
+        }
+    },
+    "required": [
+        "steps",
+        "final_answer"
+    ],
+    "additionalProperties": false
 }
 ```
 
@@ -713,40 +314,40 @@ Example of explicit recursion:
 
 ```json
 {
-	"type": "object",
-	"properties": {
-		"linked_list": {
-			"$ref": "#/$defs/linked_list_node"
-		}
-	},
-	"$defs": {
-		"linked_list_node": {
-			"type": "object",
-			"properties": {
-				"value": {
-					"type": "number"
-				},
-				"next": {
-					"anyOf": [
-						{
-							"$ref": "#/$defs/linked_list_node"
-						},
-						{
-							"type": "null"
-						}
-					]
-				}
-			},
-			"additionalProperties": false,
-			"required": [
-				"next",
-				"value"
-			]
-		}
-	},
-	"additionalProperties": false,
-	"required": [
-		"linked_list"
-	]
+    "type": "object",
+    "properties": {
+        "linked_list": {
+            "$ref": "#/$defs/linked_list_node"
+        }
+    },
+    "$defs": {
+        "linked_list_node": {
+            "type": "object",
+            "properties": {
+                "value": {
+                    "type": "number"
+                },
+                "next": {
+                    "anyOf": [
+                        {
+                            "$ref": "#/$defs/linked_list_node"
+                        },
+                        {
+                            "type": "null"
+                        }
+                    ]
+                }
+            },
+            "additionalProperties": false,
+            "required": [
+                "next",
+                "value"
+            ]
+        }
+    },
+    "additionalProperties": false,
+    "required": [
+        "linked_list"
+    ]
 }
 ```
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "構造化出力に関するドキュメントの更新"
}
```

### Explanation
この変更は、構造化出力に関する文書の更新を反映しています。特に、APIの新しいバージョンにおける構造化出力のサポートについての情報が追加され、具体的な使用例が示されています。変更の内容では、特にPython、C#、RESTにおける構造化出力の必要なパラメータと使用方法が記述されています。

これにより、開発者はそれぞれの言語やプラットフォームでの具体的な実装方法を理解しやすくなります。また、従来のコードサンプルが削除され、新しい記述形式が導入されたため、ドキュメントはより整然としていて、最新の技術に適応した内容となっています。特にゾーニングの機能が導入され、異なるプログラミング言語のセクションが明確に分けられるようになっています。全体として、この更新は機能の説明をより具体的かつ明瞭にし、利用者による理解を促進することを目的としています。

## articles/ai-services/openai/includes/assistants-ai-studio.md{#item-1632e2}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: Quickstart - getting started with Azure OpenAI assistants (preview) in Az
 titleSuffix: Azure OpenAI
 description: Walkthrough on how to get started with Azure OpenAI assistants with new features like code interpreter in Azure AI Foundry portal.
 manager: nitinme
-ms.service: azure-ai-studio
+ms.service: azure-ai-foundry
 ms.custom:
   - build-2024
   - ignite-2024
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Studioのサービス名の変更"
}
```

### Explanation
この変更は、Azure OpenAIに関連するドキュメントの「ms.service」フィールドの内容を更新するもので、サービス名が「azure-ai-studio」から「azure-ai-foundry」に変更されました。この修正により、さらに正確な情報が提供され、ユーザーが適切なサービスを認識して利用できるようになります。

その他の部分では、タイトルや説明が変更されていないため、主な変更点はこのサービス名の更新のみです。この種の変更は、ユーザーや開発者が現行のサービスに関連する正確な情報にアクセスできることを保証するために重要です。全体として、文書は継続的に最新のサービスに適合させるために維持されています。

## articles/ai-services/openai/includes/assistants-csharp.md{#item-cc4697}

<details>
<summary>Diff</summary>
````diff
@@ -24,13 +24,13 @@ ms.date: 9/27/2024
 
 ### Create a new .NET Core application
 
-1. In a console window (such as cmd, PowerShell, or Bash), use the [`dotnet new`](/dotnet/core/tools/dotnet-new) command to create a new console app with the name `azure-openai-quickstart`:
+1. In a console window (such as cmd, PowerShell, or Bash), use the [`dotnet new`](/dotnet/core/tools/dotnet-new) command to create a new console app with the name `azure-openai-assistants-quickstart`:
     
     ```dotnetcli
     dotnet new console -n azure-openai-assistants-quickstart
     ```
 
-2. Change into the directory of the newly created app folder and build the app with the [`dotnet build`](/dotnet/core/tools/dotnet-build) command:
+2. In the newly created `azure-openai-assistants-quickstart` folder, build the app with the [`dotnet build`](/dotnet/core/tools/dotnet-build) command:
 
     ```dotnetcli
     dotnet build
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": ".NET Coreアプリケーション名の変更"
}
```

### Explanation
この変更は、Azure OpenAIに関連するC#のドキュメントにおいて、新しい.NET Coreアプリケーションの作成に関する指示を更新したものです。具体的には、アプリケーションの名前が「azure-openai-quickstart」から「azure-openai-assistants-quickstart」に変更されました。

変更された指示は、アプリケーション名の更新に伴い、関連するコマンドの文言も修正されています。この修正により、開発者は新しいアプリケーション名を正確に使用できるようになり、ドキュメントが最新の情報を反映するようになっています。全体的に、これによりユーザーは混乱なく正しい手順を踏むことができるようになります。

## articles/ai-services/openai/includes/fine-tuning-openai-in-ai-studio.md{#item-723c8d}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@
  description: Include file
  author: mrbullwinkle
  ms.author: mbullwin
- ms.service: azure-ai-studio
+ ms.service: azure-ai-foundry
  ms.topic: include
  ms.date: 05/03/2024
 ms.custom: include, build-2024
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Studioのサービス名の変更"
}
```

### Explanation
この変更は、Azure OpenAIに関連するドキュメントにおいて、「ms.service」フィールドの内容を更新したものです。具体的には、サービス名が「azure-ai-studio」から「azure-ai-foundry」に変更されています。この更新により、最新のサービスに対する正確な情報が提供され、ユーザーが適切なサービスを理解し利用できるようになります。

この変更は、全体的な文書の流れや内容には大きな影響を与えませんが、サービス名のアップデートは、正確性と信頼性を確保するために重要です。適切なサービスの名称を使用することで、利用者がリソースを探しやすくなり、今後の利用がスムーズになります。

## articles/ai-services/openai/includes/model-matrix/standard-global.md{#item-17a84b}

<details>
<summary>Diff</summary>
````diff
@@ -6,31 +6,31 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions
-ms.date: 02/06/2025
+ms.date: 02/10/2025
 ---
 
-| **Region**     | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4o-realtime-preview**, **2024-12-17**   | **gpt-4o-realtime-preview**, **2024-10-01**   | **gpt-4o-audio-preview**, **2024-12-17**   | **gpt-4o-mini-realtime-preview**, **2024-12-17**   | **gpt-4**, **turbo-2024-04-09**   |
-|:-------------------|:---------------------------:|:----------------------:|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------------------------------:|:-------------------------------------------:|:----------------------------------------:|:------------------------------------------------:|:-------------------------------:|
-| australiaeast      | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
-| brazilsouth        | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
-| canadaeast         | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
-| eastus             | -                       | -                  | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
-| eastus2            | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                        | ✅                                     | ✅                                             | ✅                            |
-| francecentral      | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
-| germanywestcentral | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
-| japaneast          | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
-| koreacentral       | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
-| northcentralus     | -                       | -                  | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
-| norwayeast         | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
-| polandcentral      | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
-| southafricanorth   | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
-| southcentralus     | -                       | -                  | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
-| southindia         | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
-| spaincentral       | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
-| swedencentral      | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                        | ✅                                     | ✅                                             | ✅                            |
-| switzerlandnorth   | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
-| uaenorth           | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
-| uksouth            | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
-| westeurope         | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
-| westus             | -                       | -                  | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
-| westus3            | -                       | -                  | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | -                                    | -                                            | ✅                            |
+| **Region**     | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4o-realtime-preview**, **2024-12-17**   | **gpt-4o-realtime-preview**, **2024-10-01**   | **gpt-4o-audio-preview**, **2024-12-17**   | **gpt-4o-mini-realtime-preview**, **2024-12-17**   | **gpt-4o-mini-audio-preview**, **2024-12-17**   | **gpt-4**, **turbo-2024-04-09**   |
+|:-------------------|:---------------------------:|:----------------------:|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------------------------------:|:-------------------------------------------:|:----------------------------------------:|:------------------------------------------------:|:---------------------------------------------:|:-------------------------------:|
+| australiaeast      | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | -                                         | ✅                            |
+| brazilsouth        | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | -                                         | ✅                            |
+| canadaeast         | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | -                                         | ✅                            |
+| eastus             | -                       | -                  | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | -                                    | -                                            | -                                         | ✅                            |
+| eastus2            | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                        | ✅                                     | ✅                                             | ✅                                          | ✅                            |
+| francecentral      | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | -                                         | ✅                            |
+| germanywestcentral | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | -                                         | ✅                            |
+| japaneast          | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | -                                         | ✅                            |
+| koreacentral       | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | -                                         | ✅                            |
+| northcentralus     | -                       | -                  | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | -                                    | -                                            | -                                         | ✅                            |
+| norwayeast         | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | -                                         | ✅                            |
+| polandcentral      | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | -                                         | ✅                            |
+| southafricanorth   | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | -                                         | ✅                            |
+| southcentralus     | -                       | -                  | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | -                                    | -                                            | -                                         | ✅                            |
+| southindia         | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | -                                         | ✅                            |
+| spaincentral       | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | -                                         | ✅                            |
+| swedencentral      | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                        | ✅                                     | ✅                                             | -                                         | ✅                            |
+| switzerlandnorth   | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | -                                         | ✅                            |
+| uaenorth           | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | -                                         | ✅                            |
+| uksouth            | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | -                                         | ✅                            |
+| westeurope         | -                       | -                  | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | -                                       | -                                    | -                                            | -                                         | ✅                            |
+| westus             | -                       | -                  | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | -                                    | -                                            | -                                         | ✅                            |
+| westus3            | -                       | -                  | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                       | -                                    | -                                            | -                                         | ✅                            |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルマトリックスの更新"
}
```

### Explanation
この変更は、標準グローバルモデルマトリックスに関するドキュメントを更新したもので、主に日付情報の変更とデータの整理が含まれています。具体的には、最終更新日が「02/06/2025」から「02/10/2025」に変更されています。

また、マトリックス内の情報も整理され、新たに「gpt-4o-mini-audio-preview」というモデルが追加されています。この変更により、モデルのバージョンや地域ごとのサポート状況を明確にし、ユーザーが最新の情報をもとにより良い意思決定を行えるようにしています。全体を通じて、変更によってドキュメントの正確性と有用性が向上することが期待されます。

## articles/ai-services/openai/includes/structured-outputs-dotnet.md{#item-4dd0a4}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,321 @@
+---
+ms.service: azure-ai-openai
+ms.topic: how-to
+ms.date: 02/10/2025
+author: mrbullwinkle
+ms.author: mbullwin
+zone_pivot_groups: structured-outputs
+---
+
+## Getting started
+
+Add the following packages to your project to work with Azure OpenAI:
+
+- **[Azure.AI.OpenAI](https://www.nuget.org/packages/Azure.AI.OpenAI/)**: Provides an Azure OpenAI client with Azure specific functionality that builds on top of the standard [OpenAI](https://www.nuget.org/packages/OpenAI/) library dependency.
+- **[Azure.Identity](https://www.nuget.org/packages/Azure.Identity)**: Provides Microsoft Entra ID token authentication support across the Azure SDK libraries. 
+- **[Newtonsoft.Json.Schema](https://www.nuget.org/packages/Newtonsoft.Json.Schema)**: Provides helpful utilities for working with JSON schemas.
+
+```dotnetcli
+dotnet add package Azure.AI.OpenAI --prerelease
+dotnet add package Azure.Identity
+dotnet add package Newtonsoft.Json.Schema
+```
+
+# [Microsoft Entra ID](#tab/dotnet-entra-id)
+
+If you are new to using Microsoft Entra ID for authentication see [How to configure Azure OpenAI Service with Microsoft Entra ID authentication](../how-to/managed-identity.md).
+
+```csharp
+using Azure.AI.OpenAI;
+using Azure.Identity;
+using Newtonsoft.Json.Schema.Generation;
+using OpenAI.Chat;
+using System.ClientModel;
+
+// Create the clients
+string endpoint = GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT");
+
+AzureOpenAIClient openAIClient = new(
+    new Uri(endpoint),
+    new DefaultAzureCredential());
+
+var client = openAIClient.GetChatClient("gpt-4o");
+
+// Create a chat with initial prompts
+var chat = new List<ChatMessage>()
+    {
+         new SystemChatMessage("Extract the event information and projected weather."),
+         new UserChatMessage("Alice and Bob are going to a science fair in Seattle on June 1st, 2025.")
+    };
+
+// Get the schema of the class for the structured response
+JSchemaGenerator generator = new JSchemaGenerator();
+var jsonSchema = generator.Generate(typeof(CalendarEvent)).ToString();
+
+// Get a completion with structured output
+var chatUpdates = client.CompleteChatStreamingAsync(
+        chat,
+        new ChatCompletionOptions()
+        {
+            ResponseFormat = ChatResponseFormat.CreateJsonSchemaFormat(
+                        "calenderEvent",
+                        BinaryData.FromString(jsonSchema))
+        });
+
+// Write the structured response
+await foreach (var chatUpdate in chatUpdates)
+{
+    foreach (var contentPart in chatUpdate.ContentUpdate)
+    {
+        Console.Write(contentPart.Text);
+    }
+}
+
+// The class for the structured response
+public class CalendarEvent()
+{
+    public string Name { get; set; }
+    public string Date { get; set; }
+    public List<string> Participants { get; set; }
+}
+
+```
+
+# [Key-based auth](#tab/dotnet-keys)
+
+```csharp
+using Azure.AI.OpenAI;
+using Newtonsoft.Json.Schema.Generation;
+using OpenAI.Chat;
+using System.ClientModel;
+
+// Create the clients
+string endpoint = GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT");
+string key = GetEnvironmentVariable("AZURE_OPENAI_API_KEY");
+
+AzureOpenAIClient openAIClient = new(
+    new Uri(endpoint),
+    new ApiKeyCredential(key));
+
+var client = openAIClient.GetChatClient("gpt-4o");
+
+// Create a chat with initial prompts
+var chat = new List<ChatMessage>()
+    {
+         new SystemChatMessage("Extract the event information and projected weather."),
+         new UserChatMessage("Alice and Bob are going to a science fair in Seattle on June 1st, 2025.")
+    };
+
+// Get the schema of the class for the structured response
+JSchemaGenerator generator = new JSchemaGenerator();
+var jsonSchema = generator.Generate(typeof(CalendarEvent)).ToString();
+
+// Get a completion with structured output
+var chatUpdates = client.CompleteChatStreamingAsync(
+        chat,
+        new ChatCompletionOptions()
+        {
+            ResponseFormat = ChatResponseFormat.CreateJsonSchemaFormat(
+                        "calenderEvent",
+                        BinaryData.FromString(jsonSchema))
+        });
+
+// Write the structured response
+await foreach (var chatUpdate in chatUpdates)
+{
+    foreach (var contentPart in chatUpdate.ContentUpdate)
+    {
+        Console.Write(contentPart.Text);
+    }
+}
+
+// The class for the structured response
+public class CalendarEvent()
+{
+    public string Name { get; set; }
+    public string Date { get; set; }
+    public List<string> Participants { get; set; }
+}
+
+```
+
+---
+
+## Function calling with structured outputs
+
+Structured Outputs for function calling can be enabled with a single parameter, by supplying `strict: true`. 
+
+# [Microsoft Entra ID](#tab/dotnet-entra-id)
+
+```csharp
+using Azure.AI.OpenAI;
+using Newtonsoft.Json.Schema.Generation;
+using OpenAI.Chat;
+using System.ClientModel;
+
+// Create the clients
+string endpoint = GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT");
+
+AzureOpenAIClient openAIClient = new(
+    new Uri(endpoint),
+    new DefaultAzureCredential());
+
+var chatClient = openAIClient.GetChatClient("gpt-4o");
+
+// Local function to be used by the assistant tooling
+string GetTemperature(string location, string date)
+{
+    // Placeholder for Weather API
+    if(location == "Seattle" && date == "2025-06-01")
+    {
+        return "75";
+    }
+
+    return "50";
+}
+
+// Create a tool to get the temperature
+ChatTool GetTemperatureTool = ChatTool.CreateFunctionTool(
+    functionName: nameof(GetTemperature),
+    functionSchemaIsStrict: true,
+    functionDescription: "Get the projected temperature by date and location.",
+    functionParameters: BinaryData.FromBytes("""
+        {
+            "type": "object",
+            "properties": {
+                "location": {
+                    "type": "string",
+                    "description": "The location of the weather."
+                },
+                "date": {
+                    "type": "string",
+                    "description": "The date of the projected weather."
+                }
+            },
+            "required": ["location", "date"],
+            "additionalProperties": false  
+        }
+        """u8.ToArray())
+);
+
+// Create a chat with prompts
+var chat = new List<ChatMessage>()
+    {
+         new SystemChatMessage("Extract the event information and projected weather."),
+         new UserChatMessage("Alice and Bob are going to a science fair in Seattle on June 1st, 2025.")
+    };
+
+// Create a JSON schema for the CalendarEvent structured response
+JSchemaGenerator generator = new JSchemaGenerator();
+var jsonSchema = generator.Generate(typeof(CalendarEvent)).ToString();
+
+// Get a chat completion from the AI model
+var completion = chatClient.CompleteChat(
+        chat,
+        new ChatCompletionOptions()
+        {
+            ResponseFormat = ChatResponseFormat.CreateJsonSchemaFormat(
+                "calenderEvent",
+                BinaryData.FromString(jsonSchema)),
+            Tools = { GetTemperatureTool }
+        });
+
+Console.WriteLine(completion.Value.ToolCalls[0].FunctionName);
+
+// Structured response class
+public class CalendarEvent()
+{
+    public string Name { get; set; }
+    public string Date { get; set; }
+    public string Temperature { get; set; }
+    public List<string> Participants { get; set; }
+}
+```
+
+# [Key-based auth](#tab/dotnet-keys)
+
+```csharp
+using Azure.AI.OpenAI;
+using Newtonsoft.Json.Schema.Generation;
+using OpenAI.Chat;
+using System.ClientModel;
+
+// Create the clients
+string endpoint = GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT");
+string key = GetEnvironmentVariable("AZURE_OPENAI_API_KEY");
+
+AzureOpenAIClient openAIClient = new(
+    new Uri(endpoint),
+    new ApiKeyCredential(key));
+
+var chatClient = openAIClient.GetChatClient("gpt-4o");
+
+// Local function to be used by the assistant tooling
+string GetTemperature(string location, string date)
+{
+    // Placeholder for Weather API
+    if(location == "Seattle" && date == "2025-06-01")
+    {
+        return "75";
+    }
+
+    return "50";
+}
+
+// Create a tool to get the temperature
+ChatTool GetTemperatureTool = ChatTool.CreateFunctionTool(
+    functionName: nameof(GetTemperature),
+    functionSchemaIsStrict: true,
+    functionDescription: "Get the projected temperature by date and location.",
+    functionParameters: BinaryData.FromBytes("""
+        {
+            "type": "object",
+            "properties": {
+                "location": {
+                    "type": "string",
+                    "description": "The location of the weather."
+                },
+                "date": {
+                    "type": "string",
+                    "description": "The date of the projected weather."
+                }
+            },
+            "required": ["location", "date"],
+            "additionalProperties": false  
+        }
+        """u8.ToArray())
+);
+
+// Create a chat with prompts
+var chat = new List<ChatMessage>()
+    {
+         new SystemChatMessage("Extract the event information and projected weather."),
+         new UserChatMessage("Alice and Bob are going to a science fair in Seattle on June 1st, 2025.")
+    };
+
+// Create a JSON schema for the CalendarEvent structured response
+JSchemaGenerator generator = new JSchemaGenerator();
+var jsonSchema = generator.Generate(typeof(CalendarEvent)).ToString();
+
+// Get a chat completion from the AI model
+var completion = chatClient.CompleteChat(
+        chat,
+        new ChatCompletionOptions()
+        {
+            ResponseFormat = ChatResponseFormat.CreateJsonSchemaFormat(
+                "calenderEvent",
+                BinaryData.FromString(jsonSchema)),
+            Tools = { GetTemperatureTool }
+        });
+
+Console.WriteLine(completion.Value.ToolCalls[0].FunctionName);
+
+// Structured response class
+public class CalendarEvent()
+{
+    public string Name { get; set; }
+    public string Date { get; set; }
+    public string Temperature { get; set; }
+    public List<string> Participants { get; set; }
+}
+```
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "構造化出力のための.NETガイドの追加"
}
```

### Explanation
この変更は、Azure OpenAIサービスにおける構造化出力に関する詳細なガイドを新たに追加したものです。このドキュメントは、Azure OpenAIと併せて使用する必要なパッケージ、設定手順、そして具体的なコード例を展開しており、開発者がこれらの機能を容易に利用できるように設計されています。

ドキュメントの初めには、必要なNuGetパッケージのインストール手順が示され、次にMicrosoft Entra IDやAPIキーを使用した認証方法に関する具体的なコードスニペットが提供されています。また、構造化応答を取得するためのクライアントの作成方法や、システムメッセージの構成についても触れています。

この新機能は、特に構造化データを必要とするアプリケーションにとって役立つもので、コード例は実際のユースケースを反映し、ユーザーが迅速に実装を行えることを目的としています。この追加により、Azure OpenAIを使用した開発がさらに容易になることが期待されます。

## articles/ai-services/openai/includes/structured-outputs-python.md{#item-2734f0}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,255 @@
+---
+ms.service: azure-ai-openai
+ms.topic: how-to
+ms.date: 02/10/2025
+author: mrbullwinkle
+ms.author: mbullwin
+zone_pivot_groups: structured-outputs
+---
+
+## Getting started
+
+# [Python (Microsoft Entra ID)](#tab/python-secure)
+
+You can use [`Pydantic`](https://docs.pydantic.dev/latest/) to define object schemas in Python. Depending on what version of the [OpenAI](https://pypi.org/project/openai/) and [`Pydantic` libraries](https://pypi.org/project/pydantic/) you're running you might need to upgrade to a newer version. These examples were tested against `openai 1.42.0` and `pydantic 2.8.2`.
+
+```cmd
+pip install openai pydantic --upgrade
+```
+
+If you are new to using Microsoft Entra ID for authentication see [How to configure Azure OpenAI Service with Microsoft Entra ID authentication](../how-to/managed-identity.md).
+
+```python
+from pydantic import BaseModel
+from openai import AzureOpenAI
+from azure.identity import DefaultAzureCredential, get_bearer_token_provider
+
+token_provider = get_bearer_token_provider(
+    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
+)
+
+client = AzureOpenAI(
+  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
+  azure_ad_token_provider=token_provider,
+  api_version="2024-10-21"
+)
+
+
+class CalendarEvent(BaseModel):
+    name: str
+    date: str
+    participants: list[str]
+
+completion = client.beta.chat.completions.parse(
+    model="MODEL_DEPLOYMENT_NAME", # replace with the model deployment name of your gpt-4o 2024-08-06 deployment
+    messages=[
+        {"role": "system", "content": "Extract the event information."},
+        {"role": "user", "content": "Alice and Bob are going to a science fair on Friday."},
+    ],
+    response_format=CalendarEvent,
+)
+
+event = completion.choices[0].message.parsed
+
+print(event)
+print(completion.model_dump_json(indent=2))
+```
+
+### Output
+
+```json
+name='Science Fair' date='Friday' participants=['Alice', 'Bob']
+{
+  "id": "chatcmpl-A1EUP2fAmL4SeB1lVMinwM7I2vcqG",
+  "choices": [
+    {
+      "finish_reason": "stop",
+      "index": 0,
+      "logprobs": null,
+      "message": {
+        "content": "{\n  \"name\": \"Science Fair\",\n  \"date\": \"Friday\",\n  \"participants\": [\"Alice\", \"Bob\"]\n}",
+        "refusal": null,
+        "role": "assistant",
+        "function_call": null,
+        "tool_calls": [],
+        "parsed": {
+          "name": "Science Fair",
+          "date": "Friday",
+          "participants": [
+            "Alice",
+            "Bob"
+          ]
+        }
+      }
+    }
+  ],
+  "created": 1724857389,
+  "model": "gpt-4o-2024-08-06",
+  "object": "chat.completion",
+  "service_tier": null,
+  "system_fingerprint": "fp_1c2eaec9fe",
+  "usage": {
+    "completion_tokens": 27,
+    "prompt_tokens": 32,
+    "total_tokens": 59
+  }
+}
+```
+
+# [Python (key-based auth)](#tab/python)
+
+You can use [`Pydantic`](https://docs.pydantic.dev/latest/) to define object schemas in Python. Depending on what version of the [OpenAI](https://pypi.org/project/openai/) and [`Pydantic` libraries](https://pypi.org/project/pydantic/) you're running you might need to upgrade to a newer version. These examples were tested against `openai 1.42.0` and `pydantic 2.8.2`.
+
+```cmd
+pip install openai pydantic --upgrade
+```
+
+```python
+from pydantic import BaseModel
+from openai import AzureOpenAI
+
+client = AzureOpenAI(
+  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
+  api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
+  api_version="2024-10-21"
+)
+
+
+class CalendarEvent(BaseModel):
+    name: str
+    date: str
+    participants: list[str]
+
+completion = client.beta.chat.completions.parse(
+    model="MODEL_DEPLOYMENT_NAME", # replace with the model deployment name of your gpt-4o 2024-08-06 deployment
+    messages=[
+        {"role": "system", "content": "Extract the event information."},
+        {"role": "user", "content": "Alice and Bob are going to a science fair on Friday."},
+    ],
+    response_format=CalendarEvent,
+)
+
+event = completion.choices[0].message.parsed
+
+print(event)
+print(completion.model_dump_json(indent=2))
+```
+
+### Output
+
+```json
+name='Science Fair' date='Friday' participants=['Alice', 'Bob']
+{
+  "id": "chatcmpl-A1EUP2fAmL4SeB1lVMinwM7I2vcqG",
+  "choices": [
+    {
+      "finish_reason": "stop",
+      "index": 0,
+      "logprobs": null,
+      "message": {
+        "content": "{\n  \"name\": \"Science Fair\",\n  \"date\": \"Friday\",\n  \"participants\": [\"Alice\", \"Bob\"]\n}",
+        "refusal": null,
+        "role": "assistant",
+        "function_call": null,
+        "tool_calls": [],
+        "parsed": {
+          "name": "Science Fair",
+          "date": "Friday",
+          "participants": [
+            "Alice",
+            "Bob"
+          ]
+        }
+      }
+    }
+  ],
+  "created": 1724857389,
+  "model": "gpt-4o-2024-08-06",
+  "object": "chat.completion",
+  "service_tier": null,
+  "system_fingerprint": "fp_1c2eaec9fe",
+  "usage": {
+    "completion_tokens": 27,
+    "prompt_tokens": 32,
+    "total_tokens": 59
+  }
+}
+```
+
+---
+
+## Function calling with structured outputs
+
+Structured Outputs for function calling can be enabled with a single parameter, by supplying `strict: true`. 
+
+> [!NOTE]
+> Structured outputs are not supported with parallel function calls. When using structured outputs set `parallel_tool_calls` to `false`.
+
+# [Python (Microsoft Entra ID)](#tab/python-secure)
+
+```python
+from enum import Enum
+from typing import Union
+from pydantic import BaseModel
+import openai
+from openai import AzureOpenAI
+
+client = AzureOpenAI(
+  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
+  api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
+  api_version="2024-10-21"
+)
+
+
+class GetDeliveryDate(BaseModel):
+    order_id: str
+
+tools = [openai.pydantic_function_tool(GetDeliveryDate)]
+
+messages = []
+messages.append({"role": "system", "content": "You are a helpful customer support assistant. Use the supplied tools to assist the user."})
+messages.append({"role": "user", "content": "Hi, can you tell me the delivery date for my order #12345?"}) 
+
+response = client.chat.completions.create(
+    model="MODEL_DEPLOYMENT_NAME", # replace with the model deployment name of your gpt-4o 2024-08-06 deployment
+    messages=messages,
+    tools=tools
+)
+
+print(response.choices[0].message.tool_calls[0].function)
+print(response.model_dump_json(indent=2))
+```
+
+# [Python (key-based auth)](#tab/python)
+
+```python
+from enum import Enum
+from typing import Union
+from pydantic import BaseModel
+import openai
+from openai import AzureOpenAI
+
+client = AzureOpenAI(
+  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
+  api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
+  api_version="2024-10-21"
+)
+
+class GetDeliveryDate(BaseModel):
+    order_id: str
+
+tools = [openai.pydantic_function_tool(GetDeliveryDate)]
+
+messages = []
+messages.append({"role": "system", "content": "You are a helpful customer support assistant. Use the supplied tools to assist the user."})
+messages.append({"role": "user", "content": "Hi, can you tell me the delivery date for my order #12345?"}) 
+
+response = client.chat.completions.create(
+    model="MODEL_DEPLOYMENT_NAME", # replace with the model deployment name of your gpt-4o 2024-08-06 deployment
+    messages=messages,
+    tools=tools
+)
+
+print(response.choices[0].message.tool_calls[0].function)
+print(response.model_dump_json(indent=2))
+```
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "構造化出力のためのPythonガイドの追加"
}
```

### Explanation
この変更は、PythonにおけるAzure OpenAIサービスの構造化出力に関する新しいガイドを追加したものです。このドキュメントは、Azure OpenAIとPydanticを使用してオブジェクトスキーマを定義し、イベント情報の抽出や機能呼び出しの実行方法について詳しく説明しています。

最初に、必要なライブラリである`openai`と`pydantic`をインストールする手順が示されており、その後、Microsoft Entra IDを用いた認証方法が紹介されています。続いて、構造化出力からイベント情報を抽出するための具体的なPythonコードが提供されています。コード例では、カレンダーイベントのモデルを定義し、AIモデルを使用してそのデータを取得する流れが示されています。

また、関数呼び出しを使用した構造化出力の実装方法についても説明されており、具体的なリクエストメッセージとレスポンスの取り扱いが示されています。この変更は、開発者がAzure OpenAIの機能を簡単に利用できるようにし、実際のアプリケーションに簡単に統合できることを目的としています。ユーザーが新しい機能を効果的に活用できる基盤を提供していると言えるでしょう。

## articles/ai-services/openai/includes/structured-outputs-rest.md{#item-c2c1a0}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,180 @@
+---
+ms.service: azure-ai-openai
+ms.topic: how-to
+ms.date: 02/10/2025
+author: mrbullwinkle
+ms.author: mbullwin
+zone_pivot_groups: structured-outputs
+---
+
+## Getting started
+
+`response_format` is set to `json_schema` with `strict: true` set.
+
+```bash
+curl -X POST  https://YOUR_RESOURCE_NAME.openai.azure.com/openai/deployments/YOUR_MODEL_DEPLOYMENT_NAME/chat/completions?api-version=2024-10-21 \
+  -H "api-key: $AZURE_OPENAI_API_KEY" \
+  -H "Content-Type: application/json" \
+    -d '{
+        "messages": [
+                {"role": "system", "content": "Extract the event information."},
+                {"role": "user", "content": "Alice and Bob are going to a science fair on Friday."}
+            ],
+            "response_format": {
+                "type": "json_schema",
+                "json_schema": {
+                    "name": "CalendarEventResponse",
+                    "strict": true,
+                    "schema": {
+                        "type": "object",
+                        "properties": {
+                            "name": {
+                              "type": "string"
+                            },
+                            "date": {
+                                "type": "string"
+                            },
+                            "participants": {
+                                "type": "array",
+                                "items": {
+                                    "type": "string"
+                                }
+                            }
+                        },
+                        "required": [
+                            "name",
+                            "date",
+                            "participants"
+                        ],
+                        "additionalProperties": false
+                    }
+                }
+          }
+  }'
+```
+
+Output:
+
+```json
+{
+  "id": "chatcmpl-A1HKsHAe2hH9MEooYslRn9UmEwsag",
+  "object": "chat.completion",
+  "created": 1724868330,
+  "model": "gpt-4o-2024-08-06",
+  "choices": [
+    {
+      "index": 0,
+      "message": {
+        "role": "assistant",
+        "content": "{\n  \"name\": \"Science Fair\",\n  \"date\": \"Friday\",\n  \"participants\": [\"Alice\", \"Bob\"]\n}"
+      },
+      "logprobs": null,
+      "finish_reason": "stop"
+    }
+  ],
+  "usage": {
+    "prompt_tokens": 33,
+    "completion_tokens": 27,
+    "total_tokens": 60
+  },
+  "system_fingerprint": "fp_1c2eaec9fe"
+}
+
+```
+
+## Function calling with structured outputs
+
+```bash
+curl -X POST  https://YOUR_RESOURCE_NAME.openai.azure.com/openai/deployments/YOUR_MODEL_DEPLOYMENT_NAME/chat/completions?api-version=2024-10-21 \
+  -H "api-key: $AZURE_OPENAI_API_KEY" \
+  -H "Content-Type: application/json" \
+  -d '{
+  "messages": [
+    {
+      "role": "system",
+      "content": "You are a helpful assistant. The current date is August 6, 2024. You help users query for the data they are looking for by calling the query function."
+    },
+    {
+      "role": "user",
+      "content": "look up all my orders in may of last year that were fulfilled but not delivered on time"
+    }
+  ],
+  "tools": [
+    {
+      "type": "function",
+      "function": {
+        "name": "query",
+        "description": "Execute a query.",
+        "strict": true,
+        "parameters": {
+          "type": "object",
+          "properties": {
+            "table_name": {
+              "type": "string",
+              "enum": ["orders"]
+            },
+            "columns": {
+              "type": "array",
+              "items": {
+                "type": "string",
+                "enum": [
+                  "id",
+                  "status",
+                  "expected_delivery_date",
+                  "delivered_at",
+                  "shipped_at",
+                  "ordered_at",
+                  "canceled_at"
+                ]
+              }
+            },
+            "conditions": {
+              "type": "array",
+              "items": {
+                "type": "object",
+                "properties": {
+                  "column": {
+                    "type": "string"
+                  },
+                  "operator": {
+                    "type": "string",
+                    "enum": ["=", ">", "<", ">=", "<=", "!="]
+                  },
+                  "value": {
+                    "anyOf": [
+                      {
+                        "type": "string"
+                      },
+                      {
+                        "type": "number"
+                      },
+                      {
+                        "type": "object",
+                        "properties": {
+                          "column_name": {
+                            "type": "string"
+                          }
+                        },
+                        "required": ["column_name"],
+                        "additionalProperties": false
+                      }
+                    ]
+                  }
+                },
+                "required": ["column", "operator", "value"],
+                "additionalProperties": false
+              }
+            },
+            "order_by": {
+              "type": "string",
+              "enum": ["asc", "desc"]
+            }
+          },
+          "required": ["table_name", "columns", "conditions", "order_by"],
+          "additionalProperties": false
+        }
+      }
+    }
+  ]
+}'
+```
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "REST APIによる構造化出力ガイドの追加"
}
```

### Explanation
この変更は、Azure OpenAIサービスにおけるREST APIを使用した構造化出力に関する新しいガイドを追加したものです。このドキュメントでは、特に`json_schema`を用いたレスポンスフォーマットの設定と、関数呼び出しを行う方法について詳細に説明されています。

ガイドは、まず構造化出力を利用するための基本的なリクエストの形式を示しており、必要なHTTPヘッダーとともに`curl`コマンドを使用した具体的なPOSTリクエストの例が提供されています。リクエストデータには、メッセージの内容とともに、構造化スキーマを定義するための詳細が含まれています。これにより、ユーザーは取得したデータを正確にモデル化することが可能になります。

さらに、関数呼び出しを利用してデータクエリを実行する例が明示されており、具体的なツールやパラメータの詳細も記載されています。これによって、デベロッパーは複雑なクエリを構成し、必要なデータを効果的に取得できるようになります。

この追加は、Azure OpenAI REST APIを利用する開発者にとって、構造化出力の扱いがより容易になることを目的としており、実際のユースケースに即した具体的なコード例を提供することで、ユーザーが学びやすく実装しやすい環境を整えています。

## articles/ai-services/openai/toc.yml{#item-c945af}

<details>
<summary>Diff</summary>
````diff
@@ -245,6 +245,8 @@ items:
       href: ./tutorials/fine-tune.md
 - name: Security & Governance
   items:
+    - name: Data, privacy, and security
+      href: /legal/cognitive-services/openai/data-privacy?context=/azure/ai-services/openai/context/context
     - name: Use virtual networks
       href: ../cognitive-services-virtual-networks.md?context=/azure/ai-services/openai/context/context
     - name: Encryption of data at rest
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次の更新にデータとプライバシーセクションの追加"
}
```

### Explanation
この変更は、OpenAIに関するドキュメントの目次（toc.yml）に対して行われたマイナーな更新です。具体的には、「セキュリティとガバナンス」セクションに「データ、プライバシー、セキュリティ」という新しい項目が追加されました。この追加項目は、関連するプライバシーとセキュリティに関する情報へユーザーを誘導するリンクを含んでいます。

具体的には、新しいアイテムにはデータプライバシーに関する法律的なリソースへのハイパーリンクが提供されており、これによりユーザーはAzure OpenAIにおけるデータの取り扱いやプライバシー方針について簡単にアクセスできるようになります。この変更は、ユーザーが重要な情報を見つけやすくすることを目的としており、ドキュメントのナビゲーションを向上させる効果があります。


