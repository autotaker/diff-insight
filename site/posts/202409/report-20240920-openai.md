---
date: '2024-09-20'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e496207...MicrosoftDocs:655e817
summary: |-
  ## 要約
  今回の変更は、Azure OpenAI APIのエンドポイントに関する軽微な更新です。新たに`/chat/completions`エンドポイントが追加され、従来の`/completions`エンドポイントが削除されました。この変更により、既存の実装が影響を受ける可能性があるため、ユーザーは速やかにコードを更新し、新しいエンドポイントを利用するように移行する必要があります。また、変更内容はドキュメントやAPIリファレンスに明示的に反映されることが望まれます。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e496207...MicrosoftDocs:655e817){target="_blank"}

<format>
# ハイライト
今回の変更はAzure OpenAI APIのエンドポイントに関する軽微な更新です。重要なポイントとして、新しいエンドポイント`/chat/completions`への変更と、従来のエンドポイント`/completions`の削除が含まれています。

## 新機能
- `POST /chat/completions`エンドポイントの追加

## 互換性に影響する変更
- `POST /completions`エンドポイントの削除

## その他の更新
- 特になし

# インサイト
このコードの変更は、Azure OpenAIサービスを利用するユーザーにとって重要なアップデートです。具体的には、APIの呼び出しパスが変更されたことにより、既存の実装がそのままでは動作しなくなる可能性があります。エンドポイントの変更は新機能の導入や特定の機能の拡張の一環として行われることがよくありますが、今回のケースでは具体的な説明が無いため、その背景は明確ではありません。

新しいエンドポイント`/chat/completions`はおそらく、チャット関連の機能を強化するためのものと推測されます。チャットアプリケーションやリアルタイムコミュニケーションシステムを構築する際に、このエンドポイントを活用することで効率的なAPI呼び出しが可能になります。また、新しいエンドポイントに移行することで、サービスのパフォーマンスや拡張性が向上する可能性も考えられます。

一方で、既存の`/completions`エンドポイントを利用しているシステムにとっては、この変更が互換性に影響を与える重大な変更となります。ユーザーは速やかにコードを更新し、新しいエンドポイントを使用するように移行する必要があります。このプロセスがスムーズに進行するよう、開発者は事前に十分なテストを行い、変更の影響を最小限に抑える努力が求められます。

最後に、このようなエンドポイントの変更は、ドキュメントやAPIリファレンスでもすぐに反映されるべきです。ユーザーの混乱を避けるため、更新が行われたことを明示するアナウンスメントやガイドラインが提供されることが望まれます。以上の点を踏まえ、今回の変更がユーザーに与える影響を最小限にとどめるための対応が重要となるでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [api-surface.md](#item-a25fa2) | minor update | APIエンドポイントの変更 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/includes/api-surface.md{#item-a25fa2}

<details>
<summary>Diff</summary>
````diff
@@ -38,5 +38,5 @@ Azure OpenAI provides two methods for authentication. You can use  either API Ke
 The service APIs are versioned using the ```api-version``` query parameter. All versions follow the YYYY-MM-DD date structure. For example:
 
 ```http
-POST https://YOUR_RESOURCE_NAME.openai.azure.com/openai/deployments/YOUR_DEPLOYMENT_NAME/completions?api-version=2024-06-01
+POST https://YOUR_RESOURCE_NAME.openai.azure.com/openai/deployments/YOUR_DEPLOYMENT_NAME/chat/completions?api-version=2024-06-01
 ```
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIエンドポイントの変更"
}
```

### Explanation
このコードの変更は、Azure OpenAIのAPIにおけるエンドポイントの更新に関するものです。具体的には、API呼び出しの一部であるPOSTリクエストのパスが変更されました。元々のエンドポイントは`/completions`であったのに対し、新しいエンドポイントは`/chat/completions`に変更されています。この変更により、ユーザーがAPIを使用する際に、適切なエンドポイントを使用する必要があります。また、変更は1行の追加と1行の削除で実行されており、全体的には軽微な更新と位置付けられます。


