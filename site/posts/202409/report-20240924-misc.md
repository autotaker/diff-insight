---
date: '2024-09-24'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:89cdcc6...MicrosoftDocs:e3ea9cd
summary: この更新では、LlamaIndexとAzure AI Studioに関するドキュメントが改善され、新機能としてMicrosoft Entra IDと環境変数設定に関する具体的なコード例と、埋め込みモデル関連の簡単なテストコードが追加されました。重大な変更はありませんが、文章の明瞭化や手順の簡略化によりユーザビリティが向上しています。特に、表現が明確になり、不要なパラメータの説明が省かれたことで、ユーザーが情報をより理解しやすくなっています。このような改善は、初めてLlamaIndexを使用するユーザーや既存のユーザーにとって非常に有益です。全体として、この更新は使いやすさを高める貴重な一歩です。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:89cdcc6...MicrosoftDocs:e3ea9cd){target="_blank"}

# ハイライト
この更新では、LlamaIndexとAzure AI Studioに関連するドキュメントが改善されています。焦点を当てられた新機能と重大な変更点を以下にまとめます。

## 新機能
特に以下の新機能が追加されました：
- **コード例の追加**：Microsoft Entra IDと環境変数設定に関する具体例が追加されました。
- **簡単なテストコードの追加**：埋め込みモデルに関連するサンプルコードが追加されました。

## 重大な変更点
今回の更新で重大な変更点は特にありませんが、以下の点でユーザビリティが向上しています：
- **文章の明瞭化**：表現がより明確に修正されました。
- **手順の簡略化**：不要なパラメータ説明が省かれ、手順が簡潔になりました。

## その他の更新
- 主に表現の改善と手順の簡略化が行われました。

# インサイト
この更新は主にユーザビリティを向上させることを目的としています。そのために、特に細かな部分での表現改善や手順の簡略化が行われています。このような改善は、LlamaIndexを初めて使用するユーザーに対しても、既存のユーザーにとっても非常に有益です。

詳細に見ていくと、次のような点が重要です：

- **文章の明瞭化**：修正された「Azure AI model catalogで展開されたモデル」から「Azure AI studioのAzure AI model catalogで展開されたモデル」という表現は、Azure AI Studioのどの部分に焦点を当てるべきかを示しており、ユーザーが誤解しにくいようになっています。
- **手順の簡略化**：手順から不要な「model_name」パラメータの説明が省かれたことで、ユーザーは手順を簡単に理解することができます。特に技術的なドキュメントにおいて手順が明瞭で簡潔であることは、ユーザーエラーを減少させます。
- **コード例の強化**：具体的なコード例の追加により、ユーザーが自身の環境でどのように設定を行えばよいかが一目瞭然となります。Microsoft Entra IDと環境変数の設定方法についての具体例は、特に初心者ユーザーにとって非常に有用です。
- **新しい情報の追加**：埋め込みモデルに関連する簡単なテストコードが追加されたことで、ユーザーは実際にモデルを使用する際の手順や挙動を事前に確認できます。これにより、不明確な点が事前に解消されるため、よりスムーズな開発体験が提供されます。

全体として、この更新はLlamaIndexとAzure AI Studioの使用をより直感的で効果的にするためのものです。ドキュメントはソフトウェアやツールの使用において非常に重要な役割を果たします。このような改善は、ユーザーのエクスペリエンスを大きく向上させる一歩と言えるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [llama-index.md](#item-613372) | minor update | LlamaIndexの使用方法に関する更新 | modified | 30 | 5 | 35 | 


# Modified Contents
## articles/ai-studio/how-to/develop/llama-index.md{#item-613372}

<details>
<summary>Diff</summary>
````diff
@@ -13,7 +13,7 @@ author: eric-urban
 
 # Develop applications with LlamaIndex and Azure AI studio
 
-In this article, you learn how to use [LlamaIndex](https://github.com/run-llama/llama_index) with models deployed from the Azure AI model catalog deployed to Azure AI studio.
+In this article, you learn how to use [LlamaIndex](https://github.com/run-llama/llama_index) with models deployed from the Azure AI model catalog in Azure AI studio.
 
 Models deployed to Azure AI studio can be used with LlamaIndex in two ways:
 
@@ -49,7 +49,7 @@ To run this tutorial, you need:
 
 ## Configure the environment
 
-To use LLMs deployed in Azure AI studio, you need the endpoint and credentials to connect to it. The parameter `model_name` is not required for endpoints serving a single model, like Managed Online Endpoints. Follow these steps to get the information you need from the model you want to use:
+To use LLMs deployed in Azure AI studio, you need the endpoint and credentials to connect to it. Follow these steps to get the information you need from the model you want to use:
 
 1. Go to the [Azure AI studio](https://ai.azure.com/).
 2. Go to deployments and select the model you deployed as indicated in the prerequisites.
@@ -79,10 +79,15 @@ llm = AzureAICompletionsModel(
 )
 ```
 
+> [!TIP]
+> The parameter `model_name` in the constructor is not required for endpoints serving a single model, like serverless endpoints).
+
 Alternatively, if your endpoint support Microsoft Entra ID, you can use the following code to create the client:
 
 ```python
+import os
 from azure.identity import DefaultAzureCredential
+from llama_index.llms.azure_inference import AzureAICompletionsModel
 
 llm = AzureAICompletionsModel(
     endpoint=os.environ["AZURE_INFERENCE_ENDPOINT"],
@@ -91,14 +96,15 @@ llm = AzureAICompletionsModel(
 ```
 
 > [!NOTE]
-> > Note: When using Microsoft Entra ID, make sure that the endpoint was deployed with that authentication method and that you have the required permissions to invoke it.
+> When using Microsoft Entra ID, make sure that the endpoint was deployed with that authentication method and that you have the required permissions to invoke it.
 
 If you are planning to use asynchronous calling, it's a best practice to use the asynchronous version for the credentials:
 
 ```python
 from azure.identity.aio import (
     DefaultAzureCredential as DefaultAzureCredentialAsync,
 )
+from llama_index.llms.azure_inference import AzureAICompletionsModel
 
 llm = AzureAICompletionsModel(
     endpoint=os.environ["AZURE_INFERENCE_ENDPOINT"],
@@ -132,7 +138,7 @@ llm = AzureAICompletionsModel(
 
 ## Use LLMs models
 
-Use the `chat` endpoint for chat instruction models. The `complete` method is still available for model of type `chat-completions`. On those cases, your input text is converted to a message with `role="user"`.
+You can use the client directly or [#configure-the-models-used-by-your-code](Configure the models used by your code) in LlamaIndex. To use the model directly, use the `chat` method for chat instruction models:
 
 ```python
 from llama_index.core.llms import ChatMessage
@@ -156,9 +162,11 @@ for r in response:
     print(r.delta, end="")
 ```
 
+The `complete` method is still available for model of type `chat-completions`. On those cases, your input text is converted to a message with `role="user"`.
+
 ## Use embeddings models
 
-In the same way you create an LLM client, you can connect to an embedding model. In the following example, we are setting again the environment variable to now point to an embeddings model:
+In the same way you create an LLM client, you can connect to an embeddings model. In the following example, we are setting the environment variable to now point to an embeddings model:
 
 ```bash
 export AZURE_INFERENCE_ENDPOINT="<your-model-endpoint-goes-here>"
@@ -176,6 +184,21 @@ embed_model = AzureAIEmbeddingsModel(
 )
 ```
 
+The following example shows a simple test to verify it works:
+
+```python
+from llama_index.core.schema import TextNode
+
+nodes = [
+    TextNode(
+        text="Before college the two main things I worked on, "
+        "outside of school, were writing and programming."
+    )
+]
+response = embed_model(nodes=nodes)
+print(response[0].embedding)
+```
+
 ## Configure the models used by your code
 
 You can use the LLM or embeddings model client individually in the code you develop with LlamaIndex or you can configure the entire session using the `Settings` options. Configuring the session has the advantage of all your code using the same models for all the operations.
@@ -200,3 +223,5 @@ In general, you use a combination of both strategies.
 ## Related content
 
 * [How to get started with Azure AI SDKs](sdk-overview.md)
+* [Reference for LlamaIndex Embeddings Integration](https://llamahub.ai/l/embeddings/llama-index-embeddings-azure-inference)
+* [Reference for LlamaIndex LLMs Integration](https://llamahub.ai/l/llms/llama-index-llms-azure-inference)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "LlamaIndexの使用方法に関する更新"
}
```

### Explanation
この変更は、LlamaIndexとAzure AI Studioに関連する文書の更新です。具体的には、指示内容や細部の表現が改善され、情報がより明確に伝わるようになっています。主な変更点は以下の通りです：

1. **文章の明瞭化**: 「Azure AI model catalogで展開されたモデル」を「Azure AI studioのAzure AI model catalogで展開されたモデル」と修正し、文の意味がより明確になりました。

2. **手順の簡略化**: モデル情報を取得する手順から「model_name」パラメータに関する説明が省かれ、手順が簡潔になりました。

3. **コード例の強化**: 新しいコード例が追加され、Microsoft Entra IDを使用する際の注意点と、環境変数の設定方法が示されることで、ユーザーが具体的にどのように設定すればよいかが明示されました。

4. **新しい情報の追加**: 埋め込みモデルに関連する簡単なテストコードが追加され、ユーザーが実際にどのようにモデルを使用するかの例が提供されています。

全体として、この更新はLlamaIndexを使用する際のユーザビリティを向上させるためのものです。


