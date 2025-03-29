---
date: '2025-03-29'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:86d029a...MicrosoftDocs:50a8092
summary: このコードの差分では、ドキュメントとAPIに対する小さな更新が行われ、主に命名規則の整合性、APIバージョン情報の更新、GETリクエストエンドポイントの明確化、入力変数の誤記修正が含まれています。新機能の追加はありませんが、既存の機能はより明確に表現されています。破壊的な変更はなく、開発者は最新のドキュメントを参照することが重要です。これらの更新は、コードの可読性や保守性を向上させ、開発作業をスムーズにするためのものです。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:86d029a...MicrosoftDocs:50a8092){target="_blank"}

# Highlights
このコードの差分では、ドキュメントとAPIに対するいくつかの小さな更新が行われています。主な変更点は、データソースやタイプ名の命名規則の整合性を図ったこと、APIバージョン情報の更新、GETリクエストエンドポイントの明確化、入力変数の記述ミスの修正などです。これらはすべて、コードの明確性、可読性、メンテナンス性を向上させるための取り組みです。

## New features
- 特に新機能の追加はありませんが、既存の機能に対してより明確な表現が追加されました。

## Breaking changes
- 大きな破壊的変更はありませんが、使い方の詳細が明確化されたため、開発者が最新のドキュメントを参照することが重要です。

## Other updates
- 一貫した命名規則に基づくキー名とタイプ名の更新。
- より信頼性の高いAPIバージョン情報へのアップデート。
- GETリクエストのエンドポイントと入力変数の記述に関する修正。

# Insights
この更新は、コードの保守性と可読性を向上させるために行われました。一貫した命名規則の適用は、ドキュメントやコードを扱う開発者にとって非常に重要であり、誤解を防ぎます。また、APIバージョン情報の"or later"の追加は、将来的な互換性の保証をほのめかし、ユーザーが将来のバージョンにもスムーズに移行できることを示しています。APIエンドポイントの明確化や入力変数の修正は、特にAPIを利用している開発者にとって直接的な影響を与えるため、非常に重要な改良点となります。結果として、これらの小さな変更は、コードベース全体の信頼性と効率性を高め、日々の開発作業をよりスムーズにする効果があります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [use-your-data.md](#item-455d6e) | minor update | データソースのキー名を更新しました | modified | 1 | 1 | 2 | 
| [computer-use.md](#item-6fbca8) | minor update | コンピュータープレビューのタイプ名を更新しました | modified | 1 | 1 | 2 | 
| [reasoning.md](#item-a54b2f) | minor update | APIバージョンの情報を更新しました | modified | 2 | 2 | 4 | 
| [responses.md](#item-b9757d) | minor update | APIエンドポイントと入力変数の修正 | modified | 3 | 4 | 7 | 


# Modified Contents
## articles/ai-services/openai/concepts/use-your-data.md{#item-455d6e}

<details>
<summary>Diff</summary>
````diff
@@ -562,7 +562,7 @@ You can send a streaming request using the `stream` parameter, allowing data to
 ```json
 {
     "stream": true,
-    "dataSources": [
+    "data_sources": [
         {
             "type": "AzureCognitiveSearch",
             "parameters": {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データソースのキー名を更新しました"
}
```

### Explanation
この変更では、ドキュメント内の`dataSources`キーの名称が`data_sources`に変更されました。この修正は、コードの一貫性を保ち、より標準的な命名規則に従うためのものです。具体的には、`stream`パラメータを用いてデータをストリーミングリクエストとして送信する方法を説明しているセクションの562行目での修正です。この小さな変更は、コードの明確さを向上させ、より直感的に理解できるようにすることを目的としています。

## articles/ai-services/openai/how-to/computer-use.md{#item-6fbca8}

<details>
<summary>Diff</summary>
````diff
@@ -220,7 +220,7 @@ response_2 = client.responses.create(
     model="computer-use-preview",
     previous_response_id=response.id,
     tools=[{
-        "type": "computer-preview",
+        "type": "computer_use_preview",
         "display_width": 1024,
         "display_height": 768,
         "environment": "browser" # other possible values: "mac", "windows", "ubuntu"
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンピュータープレビューのタイプ名を更新しました"
}
```

### Explanation
この変更では、`computer-preview`というタイプ名が`computer_use_preview`に変更されました。この修正は、APIの呼び出しにおいて、より正確で一貫した命名規則を遵守することを目的としています。具体的には、220行目でのAPIクライアントの`responses.create`メソッド内の`tools`配列において行われています。この小さな変更により、コードの可読性と理解しやすさが向上するとともに、将来的なメンテナンスが容易になります。

## articles/ai-services/openai/how-to/reasoning.md{#item-a54b2f}

<details>
<summary>Diff</summary>
````diff
@@ -37,7 +37,7 @@ Azure OpenAI `o-series` models are designed to tackle reasoning and problem-solv
 
 | **Feature**     | **o3-mini**, **2025-01-31**  |**o1**, **2024-12-17**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   |
 |:-------------------|:--------------------------:|:--------------------------:|:-------------------------------:|:---:|
-| **API Version**    | `2024-12-01-preview` <br> `2025-01-01-preview`   | `2024-12-01-preview` <br> `2025-01-01-preview` | `2024-09-01-preview`  <br> `2024-10-01-preview` <br> `2024-12-01-preview`    | `2024-09-01-preview`  <br> `2024-10-01-preview` <br> `2024-12-01-preview`    |
+| **API Version**    | `2024-12-01-preview` or later <br> `2025-03-01-preview` (Recommended)   | `2024-12-01-preview` or later <br> `2025-03-01-preview` (Recommended) | `2024-09-01-preview` or later <br> `2025-03-01-preview` (Recommended)    | `2024-09-01-preview` or later <br> `2025-03-01-preview` (Recommended)    |
 | **[Developer Messages](#developer-messages)** | ✅ | ✅ | - | - |
 | **[Structured Outputs](./structured-outputs.md)** | ✅ | ✅ | - | - |
 | **[Context Window](../concepts/models.md#o-series-models)** | Input: 200,000 <br> Output: 100,000 | Input: 200,000 <br> Output: 100,000 | Input: 128,000  <br> Output: 32,768 | Input: 128,000  <br> Output: 65,536 |
@@ -320,4 +320,4 @@ To improve the performance of `Formatting re-enabled` you can further augment th
 - `Formatting re-enabled - please enclose code blocks with appropriate markdown tags.`
 - `Formatting re-enabled - code output should be wrapped in markdown.`
 
-Depending on your expected output you may need to customize your initial developer message further to target your specific use case.
\ No newline at end of file
+Depending on your expected output you may need to customize your initial developer message further to target your specific use case.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの情報を更新しました"
}
```

### Explanation
この変更では、Azure OpenAIの`o-series`モデルに関するAPIバージョン情報が更新されました。具体的には、APIバージョンの記述が従来の形式から`or later`という表現を追加した形式に変更されています。これにより、利用者が将来的なバージョンの利用を促す意図が明確になりました。この修正は37行目と320行目の2箇所で行われており、APIの利用に関する重要な情報が信頼性を持って伝わるようになっています。また、いくつかの文言がより明確に表現され、利用者にとっての理解が向上しています。このような小さな変更は、使用時の誤解を避け、ユーザーが適切な選択を行う助けとなります。

## articles/ai-services/openai/how-to/responses.md{#item-b9757d}

<details>
<summary>Diff</summary>
````diff
@@ -245,7 +245,7 @@ response = client.responses.retrieve("resp_67cb61fa3a448190bcf2c42d96f0d1a8")
 ### Microsoft Entra ID
 
 ```bash
-curl -X GET "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/{response_id}?api-version=2025-03-01-preview" \
+curl -X GET "https://YOUR-RESOURCE-NAME.openai.azure.com/openai/responses/{response_id}?api-version=2025-03-01-preview" \
   -H "Content-Type: application/json" \
   -H "Authorization: Bearer $AZURE_OPENAI_AUTH_TOKEN" 
 ```
@@ -441,7 +441,7 @@ inputs = [{"type": "message", "role": "user", "content": "Define and explain the
   
 response = client.responses.create(  
     model="gpt-4o",  # replace with your model deployment name  
-    input="inputs"  
+    input=inputs  
 )  
   
 inputs += response.output
@@ -451,7 +451,6 @@ inputs.append({"role": "user", "type": "message", "content": "Explain this at a
 
 second_response = client.responses.create(  
     model="gpt-4o",  
-    previous_response_id=response.id,  
     input=inputs
 )  
       
@@ -507,7 +506,7 @@ for output in response.output:
                 input.append(  
                     {  
                         "type": "function_call_output",  
-                        "call_id": output.id,  
+                        "call_id": output.call_id,  
                         "output": '{"temperature": "70 degrees"}',  
                     }  
                 )  
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIエンドポイントと入力変数の修正"
}
```

### Explanation
この変更では、APIエンドポイントや入力変数に関するいくつかの修正が行われました。具体的には、245行目では、OpenAI APIのGETリクエストが`{response_id}`から`responses/{response_id}`に変更され、リソースの取得に使用されるURLが明確化されました。また、441行目では、`input="inputs"`から`input=inputs`に変更され、変数の指定方法が正確に修正されています。さらに、451行目では`previous_response_id=response.id`が削除され、応答生成においての前回の応答IDの参照が削除されました。この変更は、APIの動作や結果に影響を与える可能性があるため、使用する際には注意が必要です。507行目でも、`output.id`から`output.call_id`に変更され、呼び出しIDの取得方法が明確にされています。これらの修正により、APIの使い勝手とコードの可読性が向上しています。


