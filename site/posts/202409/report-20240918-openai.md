---
date: '2024-09-18'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:135d681...MicrosoftDocs:78943fc
summary: 今回の変更では、ファインチューニングスタジオおよびそのチュートリアルに関するドキュメントが更新され、新たにデプロイメントステータス画像が追加されました。これにより、モデルのタイプやチェックポイントに関する情報が最新のものとなり、ユーザーの利便性が向上しました。新しい画像により、ユーザーはファインチューニングプロセスの進捗を視覚的に把握できるようになります。また、チュートリアルの情報も更新され、トラブルシューティングセクションの文言も修正され、全体としてドキュメントの精度とユーザビリティが向上しています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:135d681...MicrosoftDocs:78943fc){target="_blank"}

# ハイライト
今回の変更では、ファインチューニングスタジオ、およびそのチュートリアルに関するドキュメントが更新され、新しいデプロイメントステータス画像が追加されました。これにより、対応するモデルのタイプやモデルチェックポイントの情報が最新のものになり、ユーザーの利便性が向上します。

## 新機能
- ファインチューニングスタジオに新しいデプロイメントステータス画像が追加されました。この画像を使用して、ユーザーはファインチューニングプロセスの進捗を視覚的に確認することができます。

## 破壊的変更
- 特に破壊的な変更はありません。

## その他の更新
- ファインチューニングスタジオでは対応するモデルタイプの情報が更新されました。
- ファインチューニングのチュートリアルにおけるモデルチェックポイント識別子が新しいものに変更されました。
- デプロイメントデータの記述が修正され、新しいモデルチェックポイントの使用が強調されました。
- デプロイメント状況のスクリーンショットの画像ソースが新しいものに変更されました。
- トラブルシューティングセクションの文言が修正されました。

# インサイト
今回の更新によって、ドキュメントの精度とユーザビリティが大きく向上しています。特に、ファインチューニングスタジオに関する情報が整理され、対応するモデルタイプが明確になったことで、ユーザーはより的確に準備と設定を行うことができます。

デプロイメントステータス画像の追加は、ファインチューニングプロセスの視覚的な理解を容易にし、トレーニングやデプロイメントがどの段階にあるのかを一目で把握できるようになりました。このビジュアルエイドは、特にファインチューニングの各ステップを確認する際に、非常に役立ちます。

また、チュートリアルの更新によって、ユーザーが最新のモデルチェックポイントを使用できるようになり、手順の一貫性と正確性が強化されました。特に新しいモデル識別子の使用が明記されているため、古いチェックポイントとの混同が防がれます。さらに、トラブルシューティングセクションの整備により、問題解決がスムーズになることが期待されます。

全体として、この一連の更新は、ユーザーがファインチューニングプロセスをより効率的に、そして正確に実行するための大きな支えとなるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [fine-tuning-studio.md](#item-439f1e) | minor update | ファインチューニングスタジオのモデルタイプの更新 | modified | 2 | 2 | 4 | 
| [studio-deployment-status.png](#item-3cdf5c) | new feature | ファインチューニングスタジオのデプロイメントステータス画像の追加 | added | 0 | 0 | 0 | 
| [fine-tune.md](#item-8f87b5) | minor update | ファインチューニングチュートリアルの更新 | modified | 7 | 7 | 14 | 


# Modified Contents
## articles/ai-services/openai/includes/fine-tuning-studio.md{#item-439f1e}

<details>
<summary>Diff</summary>
````diff
@@ -65,9 +65,9 @@ Different model types require a different format of training data.
 
 # [chat completion models](#tab/turbo)
 
-The training and validation data you use **must** be formatted as a JSON Lines (JSONL) document. For `gpt-35-turbo-0613` the fine-tuning dataset must be formatted in the conversational format that is used by the [Chat completions](../how-to/chatgpt.md) API.
+The training and validation data you use **must** be formatted as a JSON Lines (JSONL) document. For `gpt-35-turbo` (all versions), `gpt-4`, `gpt-4o`, and `gpt-4o-mini`, the fine-tuning dataset must be formatted in the conversational format that is used by the [Chat completions](../how-to/chatgpt.md) API.
 
-If you would like a step-by-step walk-through of fine-tuning a `gpt-35-turbo-0613` model please refer to the [Azure OpenAI fine-tuning tutorial.](../tutorials/fine-tune.md)
+If you would like a step-by-step walk-through of fine-tuning a `gpt-4o-mini` (2024-07-18) model please refer to the [Azure OpenAI fine-tuning tutorial.](../tutorials/fine-tune.md)
 
 ### Example file format
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングスタジオのモデルタイプの更新"
}
```

### Explanation
このコードの変更は、ファインチューニングスタジオに関するドキュメントの一部を修正する内容です。具体的には、トレーニングおよび検証データの要件について、サポートされるモデルタイプに関する情報が更新されました。

変更点の具体的な内容としては、データのフォーマット要件が`gpt-35-turbo-0613`から、`gpt-35-turbo`のすべてのバージョン、`gpt-4`、`gpt-4o`、`gpt-4o-mini`に拡張されました。この変更により、ユーザーはさまざまなモデルタイプに対して適切なフォーマットのデータを準備することができるようになります。また、ファインチューニングモデルの具体的な例として、`gpt-4o-mini`（2024-07-18）モデルに関する手順を参照するよう更新されています。 

この修正により、ユーザーにとって有益な情報が提供され、ファインチューニングのプロセスが明確になっています。

## articles/ai-services/openai/media/tutorials/fine-tuning/studio-deployment-status.png{#item-3cdf5c}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ファインチューニングスタジオのデプロイメントステータス画像の追加"
}
```

### Explanation
このコードの変更は、ファインチューニングスタジオに関連する新しい画像ファイルの追加に関するものです。具体的には、デプロイメントステータスを示す画像が新たに追加されました。この画像は、ユーザーがファインチューニングプロセスの進捗や結果を視覚的に理解するための役割を果たします。

画像は、以下のURLでアクセス可能です：
- [デプロイメントステータス画像](https://github.com/MicrosoftDocs/azure-ai-docs/raw/78943fcb5d00c79ffe210bfc34ff6c718f922b27/articles%2Fai-services%2Fopenai%2Fmedia%2Ftutorials%2Ffine-tuning%2Fstudio-deployment-status.png)

この新しいビジュアルコンテンツの追加により、ドキュメントの説明がより直感的になり、ユーザー体験が向上します。デプロイメントステータスの視覚化は、特にプロジェクトの進行状況や成果物を確認する際に便利です。

## articles/ai-services/openai/tutorials/fine-tune.md{#item-8f87b5}

<details>
<summary>Diff</summary>
````diff
@@ -755,7 +755,7 @@ This command isn't available in the 0.28.1 OpenAI Python library. Upgrade to the
     {
       "id": "ftchkpt-148ab69f0a404cf9ab55a73d51b152de",
       "created_at": 1715743077,
-      "fine_tuned_model_checkpoint": "gpt-4o-mini-2024-07-18.ft-372c72db22c34e6f9ccb62c26ee0fbd9",
+      "fine_tuned_model_checkpoint": "gpt-4o-mini-2024-07-18.ft-0e208cf33a6a466994aff31a08aba678",
       "fine_tuning_job_id": "ftjob-372c72db22c34e6f9ccb62c26ee0fbd9",
       "metrics": {
         "full_valid_loss": 1.8258173013035255,
@@ -772,7 +772,7 @@ This command isn't available in the 0.28.1 OpenAI Python library. Upgrade to the
     {
       "id": "ftchkpt-e559c011ecc04fc68eaa339d8227d02d",
       "created_at": 1715743013,
-      "fine_tuned_model_checkpoint": "gpt-4o-mini-2024-07-18.ft-372c72db22c34e6f9ccb62c26ee0fbd9:ckpt-step-90",
+      "fine_tuned_model_checkpoint": "gpt-4o-mini-2024-07-18.ft-0e208cf33a6a466994aff31a08aba678:ckpt-step-90",
       "fine_tuning_job_id": "ftjob-372c72db22c34e6f9ccb62c26ee0fbd9",
       "metrics": {
         "full_valid_loss": 1.7958603267428241,
@@ -789,7 +789,7 @@ This command isn't available in the 0.28.1 OpenAI Python library. Upgrade to the
     {
       "id": "ftchkpt-8ae8beef3dcd4dfbbe9212e79bb53265",
       "created_at": 1715742984,
-      "fine_tuned_model_checkpoint": "gpt-4o-mini-2024-07-18.ft-372c72db22c34e6f9ccb62c26ee0fbd9:ckpt-step-80",
+      "fine_tuned_model_checkpoint": "gpt-4o-mini-2024-07-18.ft-0e208cf33a6a466994aff31a08aba678:ckpt-step-80",
       "fine_tuning_job_id": "ftjob-372c72db22c34e6f9ccb62c26ee0fbd9",
       "metrics": {
         "full_valid_loss": 1.6909511662736725,
@@ -850,7 +850,7 @@ Alternatively, you can deploy your fine-tuned model using any of the other commo
 | resource_group | The resource group name for your Azure OpenAI resource |
 | resource_name | The Azure OpenAI resource name |
 | model_deployment_name | The custom name for your new fine-tuned model deployment. This is the name that will be referenced in your code when making chat completion calls. |
-| fine_tuned_model | Retrieve this value from your fine-tuning job results in the previous step. It will look like `gpt-4o-mini-2024-07-18.ft-b044a9d3cf9c4228b5d393567f693b83`. You'll need to add that value to the deploy_data json. |
+| fine_tuned_model | Retrieve this value from your fine-tuning job results in the previous step. It will look like `gpt-4o-mini-2024-07-18.ft-0e208cf33a6a466994aff31a08aba678`. You'll need to add that value to the deploy_data json. |
 
 [!INCLUDE [Fine-tuning deletion](../includes/fine-tune.md)]
 
@@ -874,7 +874,7 @@ deploy_data = {
     "properties": {
         "model": {
             "format": "OpenAI",
-            "name": "<YOUR_FINE_TUNED_MODEL>", #retrieve this value from the previous call, it will look like gpt-4o-mini-2024-07-18.ft-b044a9d3cf9c4228b5d393567f693b83
+            "name": "<YOUR_FINE_TUNED_MODEL>", #retrieve this value from the previous call, it will look like gpt-4o-mini-2024-07-18.ft-0e208cf33a6a466994aff31a08aba678
             "version": "1"
         }
     }
@@ -894,7 +894,7 @@ print(r.json())
 
 You can check on your deployment progress in the Azure OpenAI Studio:
 
-:::image type="content" source="../media/tutorials/fine-tuning/status.png" alt-text="Screenshot of the initial DataFrame table results from the CSV file." lightbox="../media/tutorials/fine-tuning/status.png":::
+:::image type="content" source="../media/tutorials/fine-tuning/studio-deployment-status.png" alt-text="Screenshot of Deployment progress on Azure OpenAI Studio." lightbox="../media/tutorials/fine-tuning/studio-deployment-status.png":::
 
 It isn't uncommon for this process to take some time to complete when dealing with deploying fine-tuned models.
 
@@ -968,7 +968,7 @@ You can delete the deployment in [Azure OpenAI Studio](https://oai.azure.com/),
 
 ## Troubleshooting
 
-### How do I enable fine-tuning? Create a custom model is greyed out in Azure OpenAI Studio?
+### How do I enable fine-tuning? Create a custom model is grayed out in Azure OpenAI Studio
 
 In order to successfully access fine-tuning you need **Cognitive Services OpenAI Contributor assigned**. Even someone with high-level Service Administrator permissions would still need this account explicitly set in order to access fine-tuning. For more information please review the [role-based access control guidance](/azure/ai-services/openai/how-to/role-based-access-control#cognitive-services-openai-contributor).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングチュートリアルの更新"
}
```

### Explanation
このコードの変更は、ファインチューニングに関するチュートリアルのドキュメントを更新する内容です。具体的には、ファインチューニングのモデルチェックポイントに関連する情報が修正され、モデル名が新しいバージョンに変更されています。

主な変更点は以下の通りです：

1. **モデルチェックポイントの更新**: いくつかの箇所で、モデルチェックポイントの識別子が新しいものに更新されました。特に、`gpt-4o-mini-2024-07-18.ft-372c72db22c34e6f9ccb62c26ee0fbd9`から`gpt-4o-mini-2024-07-18.ft-0e208cf33a6a466994aff31a08aba678`への変更が行われています。

2. **デプロイメントデータの記述修正**: モデル名の取得保証に関する記述が更新され、具体的に新しいモデルチェックポイントが使用されることが強調されています。

3. **画像のソース変更**: デプロイメント状況のスクリーンショットの画像ソースが新しいものに変更され、正確な進捗状況を示すようになっています。

4. **トラブルシューティングセクションの文言修正**: Azure OpenAI Studioにおけるファインチューニングの有効化に関するトラブルシューティングの見出しが、英語の表記の調整が行われました。

この更新により、ファインチューニングに関する情報が最新の状態に保たれ、ユーザーが正確な手順を理解しやすくなることが期待されます。


